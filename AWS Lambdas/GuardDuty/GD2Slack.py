import json
import boto3
import requests

webHookUrl = "YOUR_SLACK_WEBHOOK_URL"
minSeverityLevel = "YOUR_MIN_SEVERITY_LEVEL"

iam = boto3.client('iam')
organizations = boto3.client('organizations')

def post_message(message):
    response = requests.post(
        webHookUrl, data=json.dumps(message),
        headers={'Content-Type': 'application/json'}
    )
    return response

def process_event(event):
    message = event
    console_url = 'https://console.aws.amazon.com/guardduty'
    finding = message['detail']['type']
    finding_description = message['detail']['description']
    account = message['detail']['accountId']
    region = message['region']
    severity = message['detail']['severity']
    
    params = {'AccountId': account}
    org_response = organizations.describe_account(**params)
    organization_name = org_response['Account']['Name'] if 'Account' in org_response else "-----"
    
    # Prepare Slack message based on severity and other details
    color = "#7CD197"  # Default color for Slack message
    if severity < 4.0:
        if minSeverityLevel != 'LOW':
            return
        severity_text = 'Low'
    elif severity < 7.0:
        if minSeverityLevel == 'HIGH':
            return
        severity_text = 'Medium'
        color = '#e2d43b'
    else:
        severity_text = 'High'
        color = '#ad0614'
    
    # Prepare Slack message attachment
    attachment = {
        "fallback": f"{finding} - {console_url}/home?region={region}#/findings?search=id%3D{message['detail']['id']}",
        "pretext": f"Finding in {region} for AWS account: *{organization_name}*",
        "title": finding,
        "title_link": f"{console_url}/home?region={region}#/findings?search=id%3D{message['detail']['id']}",
        "text": finding_description,
        "color": color,
        "fields": [
            {"title": "Account Name", "value": organization_name, "short": True},
            {"title": "Severity", "value": severity_text, "short": True},
            {"title": "Region", "value": region, "short": True},
            # Add more fields as needed
        ]
    }
    
    slack_message = {
        "username": "AWS Intrusion Detection Bot",
        "attachments": [attachment]
    }
    
    # Send Slack message
    post_message(slack_message)

def lambda_handler(event, context):
    print(event)
    process_event(event)
