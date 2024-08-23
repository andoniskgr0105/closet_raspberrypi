from twilio.rest import Client

TWILIO_ACCOUNT_SID='AC2b660f95ea50df1fa5cd9f9679dfc8e4'
TWILIO_TOKEN='0d9a587d24c91877336f5edea6862e22'
TWILIO_PHONE='+12564488301'
TO_PHONE_NUMBER='+306972895618'

class SMSSender:
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID,TWILIO_TOKEN )

    def send_sms(self, message):
        try:
            self.client.messages.create(
                body=message,
                from_=TWILIO_PHONE,
                to=TO_PHONE_NUMBER
            )
            print(f"SMS sent: {message}")
        except Exception as e:
            print(f"Failed to send SMS: {e}")
