from twilio.rest import Client
import os

TWILIO_SID = os.environ["twilio_sid"]
TWILIO_AUTH_TOKEN = os.environ["twilio_auth_token"]
TWILIO_VIRTUAL_NUMBER = os.environ["twilio_virtual_number"]
TWILIO_VERIFIED_NUMBER = os.environ["receiver_phone_number"]

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)