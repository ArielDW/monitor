import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Twilio",
    from_="+16089339250",
    to="+525520270281"
)

print(message.sid)
