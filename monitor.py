import os
import time


def get_cpu_usage():
    load = os.system('uptime')
    print(load)


get_cpu_usage()
