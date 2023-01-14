import json
import os

if not os.path.exists("settings.json"):
    settings = {"CPU": "95",
                "RAM": "95",
                "email": "user@example.com"}

    with open("settings.json", "w") as f:
        json.dump(settings, f)

else:
    with open("settings.json", "r") as f:
        settings = json.load(f)

# Menu
print(f"Select an option:")
print(f"1. Update CPU threshold........Current value: {settings['CPU']} %")
print(f"2. Update memory threshold.....Current value: {settings['RAM']} %")
print(f"3. Update notification email...Current value: {settings['email']}")
print(f"4. Back")
choice = int(input("> "))

if choice == 1:
    print("\nExample: A value of 130 percent triggers an alert if 30 percent of the processes are waiting for CPU time. \n")
    new_cpu = input("Enter new CPU threshold: ")
    settings["CPU"] = new_cpu

elif choice == 2:
    new_ram = input("Enter new memory threshold: ")
    settings["RAM"] = new_ram

elif choice == 3:
    new_email = input("Enter new notification email: ")
    settings["email"] = new_email

elif choice == 4:
    pass  # add code to go back to main menu
else:
    print("Invalid choice")

# Update settings in the JSON file
settings["example"] = "new value"
with open("settings.json", "w") as f:
    json.dump(settings, f)
