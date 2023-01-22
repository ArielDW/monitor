import datetime
import os

if not os.path.exists("system_records.log"):
    with open("system_records.log", "w") as log_file:
        timestamp = str(datetime.datetime.now())
        log_file.write(timestamp + "\n")
        print("New file created")
else:
    with open("system_records.log", "a") as log_file:
        timestamp = str(datetime.datetime.now())
        log_file.write(timestamp + "\n")
        print("OK")
