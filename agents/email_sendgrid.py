# https://www.twilio.com/docs/sendgrid/for-developers/sending-email/quickstart-python
# -- NOT WORKING -- have to check maybe because the email is not existing info@mahernatout.com

import sendgrid
from dotenv import load_dotenv
import os
from sendgrid.helpers.mail import Mail, Email, To, Content


load_dotenv()
sg = sendgrid.SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))

# print("key is: "+ sg.api_key)



from_email = Email("info@mahernatout.com")  # Change to your verified sender
to_email = To("toutzi@hotmail.com")  # Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)

