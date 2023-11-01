import requests
import json
import time

def query_virustotal(ip_address, api_key):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {
        "x-apikey": api_key
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data for IP: {ip_address}")
        return None

def generate_report(data):
    report = []
    
    if data:
        attributes = data.get('data', {}).get('attributes', {})
        
        # Basic Info
        report.append(f"IP Address: {ip_address}")
        report.append(f"ASN: {attributes.get('asn', 'N/A')}")
        report.append(f"Country: {attributes.get('country', 'N/A')}")
        
        # Confidence Score
        total_engines = attributes.get('last_analysis_stats', {}).get('total', 0)
        malicious_engines = attributes.get('last_analysis_stats', {}).get('malicious', 0)
        if total_engines:
            confidence_score = (malicious_engines / total_engines) * 100
        else:
            confidence_score = 0
        report.append(f"Confidence Score: {confidence_score}%")
        
        # Detailed Scan Results
        report.append("Scan Results:")
        for engine, result in attributes.get('last_analysis_results', {}).items():
            report.append(f"  - {engine}: {result.get('result')}")
        
        return "\n".join(report)
    else:
        return "No data available"

def send_to_slack(report, ip_address, webhook_url):
    slack_data = {
        "text": f"VirusTotal Detailed Report for {ip_address}:\n```{report}```"
    }
    
    response = requests.post(
        webhook_url, 
        data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    
    if response.status_code != 200:
        print(f"Failed to send data to Slack: {response.content}")

if __name__ == "__main__":
    # Your VirusTotal API key
    api_key = "1f9a2e388e5d8c7c80026b000d0f2051f09cc99c129592d32ba331bba4f3a3dc"
    
    # Your Slack Webhook URL
    webhook_url = "https://hooks.slack.com/services/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"
    
    # List of IP addresses to check
    ip_addresses = [
        "23.105.182.19", "104.251.211.122", "202.59.10.100", "162.210.194.35",
        "198.16.66.124", "198.16.66.156", "198.16.70.28", "198.16.74.203",
        "198.16.74.204", "198.16.74.205", "198.98.49.203", "2.56.164.52",
        "207.244.71.82", "207.244.71.84", "207.244.89.161", "207.244.89.162",
        "23.106.249.52", "23.106.56.11", "23.106.56.21", "23.106.56.36",
        "23.106.56.37", "23.106.56.38", "23.106.56.54"
    ]
    
    for ip_address in ip_addresses:
        data = query_virustotal(ip_address, api_key)
        report = generate_report(data)
        
        print(f"VirusTotal Report for {ip_address}:")
        print(report)
        
        send_to_slack(report, ip_address, webhook_url)
        
        # Sleep for a few seconds to avoid hitting rate limits
        time.sleep(15)

