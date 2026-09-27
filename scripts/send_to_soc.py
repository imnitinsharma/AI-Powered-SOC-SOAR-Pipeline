import requests
import json
import time

# Corrected Production n8n Webhook URL (using /webhook/ instead of /webhook-test/)
WEBHOOK_URL = "https://nits45.app.n8n.cloud/webhook/soc-alert-ingress"

def send_security_alert():
    payload = {
        "source_ip": "185.220.101.5",
        "severity": "high",
        "cloud_provider": "AWS",
        "event_name": "UnauthorizedConsoleAccess",
        "raw_log": "Critical: Suspicious root login attempt detected from known malicious Tor exit node IP."
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        print(f"Alert sent to n8n! Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Failed to connect to n8n: {e}")

if __name__ == "__main__":
    print("Starting SOC Log Forwarder on Ubuntu VM...")
    send_security_alert()
