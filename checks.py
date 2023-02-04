import psutil
import datetime
import requests
import socket


def get_timestamp():
    return str(datetime.datetime.now())


def get_cpu_load():
    cpu = psutil.getloadavg()
    cpu_load = round(100*(cpu[0]), 2)
    return str(cpu_load)


def get_total_memory():
    memory = psutil.virtual_memory()
    total = round(memory.total / 1024 ** 2, 2)
    return str(total)


def get_free_memory():
    memory = psutil.virtual_memory()
    free = round(memory.free / 1024 ** 2, 2)
    return str(free)


def get_http_status_code(url):
    status_code = ""
    response = requests.get(url)
    if response.status_code == 200:
        return "200"
    else:
        return f'Exception: {response.status_code} {response.reason}'


def check_dns_resolution(hostname, expected_ip):
    ip_address = socket.gethostbyname(hostname)
    if ip_address == expected_ip:
        return "OK"
    else:
        return f'DNS exception: {ip_address}. Expected: {expected_ip}'
