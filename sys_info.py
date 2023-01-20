import platform
import psutil
import os


def get_system_info():
    os.system("clear")
    print("System information")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Hostname: {platform.node()}")

    cpu_load = psutil.getloadavg()
    print("CPU load average")
    print(
        f"Past 1 min: {round(cpu_load[0],2)}%, 5 mins: {round(cpu_load[1],2)}%, 15 mins: {round(cpu_load[2],2)}%")

    memory = psutil.virtual_memory()
    total = round(memory.total/1024**2, 2)
    free = round(memory.free/1024**2, 2)
    used = total - free
    percentage = round(used/total*100, 2)
    print("Memory usage")
    print(
        f"total {total} MB, free {free} MB, used {round(used,2)} MB ({percentage}%)")


def main():
    get_system_info()


if __name__ == "__main__":
    main()
