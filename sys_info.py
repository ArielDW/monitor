import os
import time


def get_systen_load():
    print("\n")
    print("System information")
    system_info = open("/etc/os-release", "r")

    sysinfo = system_info.readlines()
    print(f"OS: {sysinfo[6].split('=')[1]}")

    system_info.close()

    hostname = open("/etc/hostname", "r")
    hn = hostname.read().split()[0]
    print(f"Hostname: {hn}")
    hostname.close()

    cpu_load = open("/proc/loadavg", "r")
    load = (cpu_load.read().split()[:3]) * 100
    print("CPU load")
    print(
        f"1 min avg: {100*float(load[0])}%, 5 mins avg: {100*float(load[1])}%, 15 mins avg: {100*float(load[2])}%")
    cpu_load.close()

    memory = open("/proc/meminfo", "r")
    rows = memory.readlines()
    total = round(int(rows[0].split()[1])/1024, 2)
    free = round(int(rows[1].split()[1])/1024, 2)
    used = total - free
    percentage = round(used/total*100, 2)
    print("Memory usage")
    print(
        f"total {total} MB, free {free} MB, used {round(used,2)} MB ({percentage}%)")
    memory.close()


def main():
    get_systen_load()


if __name__ == "__main__":
    main()
