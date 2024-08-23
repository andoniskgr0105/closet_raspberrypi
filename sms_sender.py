# from twilio.rest import Client



# class SMSSender:
#     def __init__(self):
#         self.client = Client('AC2b660f95ea50df1fa5cd9f9679dfc8e4', '0d9a587d24c91877336f5edea6862e22')

#     def send_sms(self, message):
#         try:
#             self.client.messages.create(
#                 body=message,
#                 from_='+12564488301',
#                 to='+306972895618'
#             )
#             print(f"SMS sent: {message}")
#         except Exception as e:
#             print(f"Failed to send SMS: {e}")
