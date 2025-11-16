from mailersend import MailerSendClient, EmailBuilder
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
email_from = os.getenv('MAILERSEND_EMAIL_FROM')
email_to = os.getenv('MAILERSEND_EMAIL_TO')

ms = MailerSendClient()

email = (EmailBuilder()
         .from_email(email_from, "Info")
         .to_many([{"email": email_to, "name": "Mr Maher"}])
         .subject("Hello from MailerSend!")
         .html("Hello World!")
         .text("Hello World!")
         .build())

response = ms.emails.send(email)
print(f"Email sent: {response.message_id}")