import base64
from email.mime.text import MIMEText
import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            from google.auth.transport.requests import Request
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("gmail", "v1", credentials=creds)
    return service

def send_email(to_email: str, subject: str, body: str) -> str:
    """Send an email using Gmail API."""
    try:
        service = get_gmail_service()

        message = MIMEText(body)
        message["to"] = to_email
        message["subject"] = subject
        
        # Gmail API requires raw message to be base64url encoded
        create_message = {
            'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()
        }

        send_message = (service.users().messages().send(userId="me", body=create_message).execute())
        return f"✅ Email sent successfully to {to_email} via Gmail. Message Id: {send_message['id']}"
    except HttpError as error:
        return f"❌ An HTTP error occurred: {error}"
    except Exception as e:
        return f"❌ Error: {str(e)}"
