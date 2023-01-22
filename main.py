import os
import platform
import psutil


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


def menu():
    os.system("clear")
    get_system_info()
    print("\n")
    print("Choose an option:")
    print("1. Refresh system information")
    print("2. Alert settings")
    print("3. Start daemon")
    print("4. Stop daemon")
    print("5. Exit")

    choice = int(input("> "))

    if choice == 1:
        os.system("clear")
        menu()
    elif choice == 2:
        from settings import update_settings
        update_settings()
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        exit()

    else:
        print("Invalid choice")
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()
