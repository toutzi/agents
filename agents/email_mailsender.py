from mailersend import MailerSendClient, EmailBuilder
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ms = MailerSendClient()

email = (EmailBuilder()
         .from_email("MS_TRMTcO@mahernatout.com", "Info")
         .to_many([{"email": "toutzi@hotmail.com", "name": "Mr Maher"}])
         .subject("Hello from MailerSend!")
         .html("Hello World!")
         .text("Hello World!")
         .build())

response = ms.emails.send(email)
print(f"Email sent: {response.message_id}")