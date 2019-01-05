from user import User
import menu

if __name__ == '__main__':
    user = User.create_or_get_user_from_file()
    print("Hello, {}.\n".format(user.username))

    while True:
        menu.show_main_menu()
        user_input = input("> ")
        if user_input.lower() == "a":
            user.create_users_task()
        elif user_input.lower() == "b":
            while True:
                menu.show_search_menu()
                user_input = input("> ")
                if user_input == "a":
                    tasks = user.search_by_exact_date()
                    print(tasks)
                elif user_input.lower() == "e":
                    break
                else:
                    print("Invalid entry. Please retry!")

        elif user_input.lower() == "c":
            print("Thanks for using the Work Log program!")
            print("Come again soon.")
            break
        else:
            print("Invalid entry. Please retry!")

