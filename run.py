import os


def menu():
    os.system("clear")
    from sys_info import get_system_info
    get_system_info()
    print("\n")
    print("Select an option:")
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
        from update_settings import update_settings
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
