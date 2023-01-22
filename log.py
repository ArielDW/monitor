import datetime
import os
import psutil
import time
import json


def add_log_entry():
    with open("system_records.log", "a") as log_file:
        # TIMESTAMP
        timestamp = str(datetime.datetime.now())

        # CPU LOAD
        cpu = psutil.getloadavg()
        cpu_load = round(100*(cpu[0]), 2)

        # MEMORY USAGE
        memory = psutil.virtual_memory()
        total = round(memory.total/1024**2, 2)
        free = round(memory.free/1024**2, 2)
        used = total - free
        percentage = round(used/total*100, 2)
        log_file.write(
            f'{timestamp}, {str(cpu_load)} %, {total} MB, {free} MB, {round(used,2)} MB, {percentage} %\n')


def log_activity():
    if not os.path.exists("system_records.log"):
        with open("system_records.log", "w") as log_file:
            log_file.write(
                f'timestamp, cpu_load, total_memory, free_memory, used_memory, memory_utilization  \n')
            add_log_entry()
    else:
        with open("system_records.log", "a") as log_file:
            add_log_entry()


def main():
    while True:
        with open("settings.json", "r") as f:
            settings = json.load(f)
            keep_alive = settings["keep_alive"]
            if keep_alive == "True":
                log_activity()
                time.sleep(5)
            else:
                break


main()
