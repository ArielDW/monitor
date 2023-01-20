import os


def menu():
    os.system("clear")
    print("Select an option:")
    print("1. System information")
    print("2. Alert settings")
    print("3. Start daemon")
    print("4. Stop daemon")
    print("5. Exit")

    choice = int(input("> "))

    if choice == 1:
        from sys_info import get_systen_load
        get_systen_load()
    elif choice == 2:
        from update_settings import update_settings
        update_settings()
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass

    else:
        print("Invalid choice")
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()
