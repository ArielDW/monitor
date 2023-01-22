import json
import os
from main import menu


def update_settings():
    if not os.path.exists("settings.json"):
        settings = {"CPU": "95",
                    "RAM": "95",
                    "phone": "Empty",
                    "twilio_account_sid": "Empty",
                    "twilio_auth_token": "Empty",
                    "twilio_number": "Empty"}

        with open("settings.json", "w") as f:
            json.dump(settings, f)

    else:
        with open("settings.json", "r") as f:
            settings = json.load(f)

    # Menu
    os.system("clear")
    print(f"Select an option:")
    print(
        f"1. Update CPU threshold......Current value: {settings['CPU']} %")
    print(
        f"2. Update memory threshold...Current value: {settings['RAM']} %")
    print(
        f"3. Update SMS alert number...Current value: {settings['phone']}")
    print(
        f"4. Twilio account SID........Current value: {settings['twilio_account_sid']}")
    print(
        f"5. Twilio auth token.........Current value: {settings['twilio_auth_token']}")
    print(
        f"6. Twilio phone number.......Current value: {settings['twilio_number']}")

    print(f"7. Back")
    choice = int(input("> "))

    if choice == 1:
        os.system("clear")
        print("\nExample: A value of 130 percent triggers an alert if 30 percent of the processes are waiting for CPU time. \n")
        new_cpu = input("Enter new CPU threshold: ")
        settings["CPU"] = new_cpu

    elif choice == 2:
        os.system("clear")
        new_ram = input("Enter new memory threshold: ")
        settings["RAM"] = new_ram

    elif choice == 3:
        os.system("clear")
        print('\nPlease use country code and no spaces eg. +13236569090 \n')
        new_phone = input("Enter phone number to receive SMS notifications: ")
        settings["phone"] = new_phone

    elif choice == 4:
        os.system("clear")
        new_sid = input("Update Twilio account SID: ")
        settings["twilio_account_sid"] = new_sid

    elif choice == 5:
        os.system("clear")
        new_token = input("Update Twilio authorization token: ")
        settings['twilio_auth_token'] = new_token

    elif choice == 6:
        os.system("clear")
        print('\nThis is the number that you get in the Twilio website. \nPlease use country code and no spaces eg. +13236569090 \n')
        twilio_num = input(
            "Enter the Twilio number that will deliver SMS notifications: ")
        settings['twilio_number'] = twilio_num

    elif choice == 7:
        os.system("clear")
        menu()
    else:
        os.system("clear")

    with open("settings.json", "w") as f:
        json.dump(settings, f)
    update_settings()
