import sys
import os
import requests

# Load env file manually for the test script
with open("cognitive_assistant/.env", "r") as f:
    for line in f:
        if line.strip() and not line.startswith("#"):
            k, v = line.strip().split("=", 1)
            os.environ[k] = v

api_token = os.getenv("MAILTRAP_API_TOKEN")
inbox_id = os.getenv("MAILTRAP_INBOX_ID")
sender_email = os.getenv("SENDER_EMAIL")

url = f"https://sandbox.api.mailtrap.io/api/send/{inbox_id}"

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

payload = {
    "from": {"email": sender_email},
    "to": [{"email": "test@example.com"}],
    "subject": "Test",
    "text": "Body"
}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.text)
