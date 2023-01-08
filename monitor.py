import os
import time

# Assumes a 1 core system


def get_cpu_load():
    cpu_load = open("/proc/loadavg", "r")
    load = cpu_load.read().split()[:3]
    print(f"CPU; 1 min: {load[0]}%, 5 mins: {load[1]}%, 15 mins: {load[2]}%")
    cpu_load.close()


def get_memory_usage():
    memory = open("/proc/meminfo", "r")
    rows = memory.readlines()
    total = int(rows[0].split()[1])
    free = int(rows[1].split()[1])
    used = total - free
    percentage = used / total * 100
    print(f"RAM; total {total}, free {free}, used {used} ({percentage}%)")
    memory.close()


def get_storage_utilization():
    storage_utilization = os.system('')


get_cpu_load()
get_memory_usage()
get_storage_utilization()
