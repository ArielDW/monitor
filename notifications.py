import os
import json
from twilio.rest import Client

# retreives information from json file
try:
    with open("settings.json", "r") as f:
        settings = json.load(f)
        account_sid = f"{settings['twilio_account_sid']}"
        auth_token = f"{settings['twilio_auth_token']}"

        # Pending...
        '''
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Hello from Twilio",
            from_="+16089339250",
            to="+525520270281"
        )

    print(message.sid)
    '''
except IOError as error:
    import sys
    print("Error: Notification failed", error, file=sys.stderr)
    sys.exit(4)
