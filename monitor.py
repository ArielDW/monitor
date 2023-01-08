import os
import time

# Assumes a 1 core system


def get_cpu_load():
    cpu_load = open("/proc/loadavg", "r")
    load = cpu_load.read().split()[:3]
    print(
        f"CPU; 1 min avg: {load[0]}%, 5 mins avg: {load[1]}%, 15 mins avg: {load[2]}%")
    cpu_load.close()


def get_memory_usage():
    memory = open("/proc/meminfo", "r")
    rows = memory.readlines()
    total = round(int(rows[0].split()[1])/1024, 2)
    free = round(int(rows[1].split()[1])/1024, 2)
    used = total - free
    percentage = round(used/total*100, 2)
    print(
        f"RAM; total {total} MB, free {free} MB, used {used} MB ({percentage}%)")
    memory.close()


def get_storage_utilization():
    storage_utilization = os.system('')


get_cpu_load()
get_memory_usage()
get_storage_utilization()
