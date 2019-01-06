from user import User
import menu

if __name__ == '__main__':
    # Get users detail
    username = input("Enter your username: ")
    user = User.create_or_get_user_from_file(username)

    while True:
        menu.show_main_menu(user.username)
        user_input = input("> ")
        if user_input.lower() == "a":
            # Creating new task
            user.create_users_task()
            # Save it to the file
            user.write_json_file()
        elif user_input.lower() == "b":
            # Searching operations
            while True:
                menu.show_search_menu()
                user_input = input("> ")
                if user_input == "a":
                    tasks = user.search_by_date()
                    user.display_tasks(tasks)
                elif user_input == "b":
                    tasks = user.search_by_time_spent()
                    user.display_tasks(tasks)
                elif user_input == "c":
                    tasks = user.search_by_keywords()
                    user.display_tasks(tasks)
                elif user_input == "d":
                    tasks = user.search_by_pattern()
                    user.display_tasks(tasks)
                elif user_input == "e":
                    tasks = user.search_by_date_range()
                    user.display_tasks(tasks)
                elif user_input.lower() == "f":
                    break
                else:
                    print("Invalid entry. Please retry!")
        elif user_input.lower() == "c":
            # Save data to json before quiting
            user.write_json_file()
            print("Thanks for using the Work Log program!")
            print("Come again soon.")
            break
        else:
            print("Invalid entry. Please retry!")
