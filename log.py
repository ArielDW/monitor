import datetime
import os


def add_entry():
    with open("system_records.log", "a") as log_file:
        timestamp = str(datetime.datetime.now())
        log_file.write(timestamp + "\n")
        print("OK")


def log_activity():
    if not os.path.exists("system_records.log"):
        with open("system_records.log", "w") as log_file:
            add_entry()
    else:
        with open("system_records.log", "a") as log_file:
            add_entry()


log_activity()
