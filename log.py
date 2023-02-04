#!/opt/anaconda3/bin/python

from checks import *
import requests
import socket
import json
import time
import os


def add_log_entry():
    with open("system_records.log", "a") as log_file:
        timestamp = get_timestamp()
        cpu_load = get_cpu_load()
        total = get_total_memory()
        free = get_free_memory()
        #used = str(round(float(total) - float(free), 2))
        #percentage = str(round(float(used) / float(total) * 100, 2))
        status_code = get_http_status_code("https://www.google.com")
        dns_test = check_dns_resolution(
            hostname="www.google.com", expected_ip="142.251.34.142")

        log_file.write(
            f'{timestamp}, {cpu_load} %, total {total} MB, free {free} MB, HTTP {status_code}, {dns_test} \n')


def check_log_file():
    if not os.path.exists("system_records.log"):
        with open("system_records.log", "w") as log_file:
            log_file.write(
                f'timestamp, cpu_load, total_memory, free_memory, http_respose, DNS_test\n')
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
                check_log_file()
                time.sleep(5)
            else:
                break


main()
