import json
import os
from run import menu


def update_settings():
    if not os.path.exists("settings.json"):
        settings = {"CPU": "95",
                    "RAM": "95",
                    "phone": "Not set"}

        with open("settings.json", "w") as f:
            json.dump(settings, f)

    else:
        with open("settings.json", "r") as f:
            settings = json.load(f)

    # Menu
    os.system("clear")
    print(f"Select an option:")
    print(
        f"1. Update CPU threshold...............Current value: {settings['CPU']} %")
    print(
        f"2. Update memory threshold............Current value: {settings['RAM']} %")
#    print(
#        f"3. Update notification email..........Current value: {settings['email']}")
    print(
        f"3. Update notification phone number...Current value: {settings['phone']}")
    print(f"4. Back")
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

#    elif choice == 3:
#        new_email = input("Enter new notification email: ")
#        settings["email"] = new_email

    elif choice == 3:
        os.system("clear")
        print('\nPlease use country code and no spaces eg. +13236569090 \n')
        new_phone = input("Enter new phone number for SMS notifications: ")
        settings["phone"] = new_phone

    elif choice == 4:
        os.system("clear")
        menu()
    else:
        os.system("clear")
        update_settings()
