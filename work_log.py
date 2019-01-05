from user import User
import menu

if __name__ == '__main__':
    # Get users detail
    user = User.create_or_get_user_from_file()
    print("\nHello, {}.\n".format(user.username))

    while True:
        menu.show_main_menu()
        user_input = input("> ")
        if user_input.lower() == "a":
            # Creating new task
            user.create_users_task()
            user.write_json_file()
        elif user_input.lower() == "b":
            # Searching tasks
            while True:
                menu.show_search_menu()
                user_input = input("> ")
                if user_input == "a":
                    tasks = user.search_by_date()
                    print(tasks)
                elif user_input == "b":
                    tasks = user.search_by_time_spent()
                    print(tasks)
                elif user_input == "c":
                    tasks = user.search_by_keywords()
                    for task in tasks:
                        print(task)
                elif user_input == "d":
                    tasks = user.search_by_pattern()
                    for task in tasks:
                        print(task)
                elif user_input == "e":
                    tasks = user.search_by_date_range()
                    for task in tasks:
                        print(task)
                elif user_input.lower() == "f":
                    break
                else:
                    print("Invalid entry. Please retry!")

        elif user_input.lower() == "c":
            print("Thanks for using the Work Log program!")
            print("Come again soon.")
            break
        else:
            print("Invalid entry. Please retry!")
