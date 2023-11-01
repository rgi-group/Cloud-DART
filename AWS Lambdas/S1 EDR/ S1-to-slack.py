import json
import requests
import os
import logging
import boto3

# Initialize logger and DynamoDB
logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SentinelOne_Last_Alert')

def lambda_handler(event, context):
    try:
        # Slack Webhook URL from environment variable
        slack_webhook_url = os.environ.get('SLACK_WEBHOOK_URL', '')
        if not slack_webhook_url:
            logger.error("Slack Webhook URL not set.")
            return {'statusCode': 400, 'body': json.dumps('Slack Webhook URL not set.')}

        # Fetch the last alert ID from DynamoDB
        last_alert_id = table.get_item(Key={'id': 1}).get('Item', {}).get('last_alert_id', 0)

        # Query SentinelOne API for new alerts
        sentinelone_api_url = 'https://<sentinelone-api>/alerts'
        headers = {'Authorization': 'API_KEY'}
        response = requests.get(sentinelone_api_url, headers=headers)
        alerts = response.json().get('data', [])

        # Process and send each new alert to Slack
        for alert in alerts:
            alert_id = alert.get('id', 0)
            if alert_id > last_alert_id:
                # Prepare Slack message payload
                slack_message = {
                    "text": f"SentinelOne Alert: {alert.get('alert_name', 'Unknown')}",
                    "attachments": [
                        {
                            "title": "Alert Details",
                            "fields": [
                                {"title": "Threat Name", "value": alert.get('threat_name', 'N/A')},
                                {"title": "Machine Name", "value": alert.get('machine_name', 'N/A')},
                                {"title": "Severity", "value": alert.get('severity', 'N/A')}
                            ]
                        }
                    ]
                }
                # Send message to Slack
                requests.post(slack_webhook_url, json=slack_message)
                # Update the last alert ID in DynamoDB
                table.put_item(Item={'id': 1, 'last_alert_id': alert_id})

        return {'statusCode': 200, 'body': json.dumps('Alerts processed.')}

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps('An error occurred.')}
