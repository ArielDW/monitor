import os
import json
from twilio.rest import Client

# It works, disable it for now
"""
def triggerSMS(message):
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
            account_sid = f"{settings['twilio_account_sid']}"
            auth_token = f"{settings['twilio_auth_token']}"
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=message,
                from_=f'{settings["twilio_number"]}',
                to=f'{settings["phone"]}'
            )

        print(message.sid)

    except IOError as error:
        import sys
        print("Error: Notification failed", error, file=sys.stderr)
        sys.exit(4)
"""

#triggerSMS("This example works")
