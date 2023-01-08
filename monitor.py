import os
import time


def get_cpu_usage():
    cpu_load = os.system('uptime')
    print(cpu_load)


def get_memory_usage():
    mem = os.system('free -m')
    print(mem)
