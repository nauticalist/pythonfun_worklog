from utils import clear_screen


def show_main_menu(username):
    """
    Display main menu to user
    """
    welcome_text = "What would you like to do {}?".format(username.title())
    clear_screen()
    print("*"*len(welcome_text))
    print(welcome_text)
    print("*"*len(welcome_text))
    print("""
a) Add new entry?
b) Search in existing entries
c) Quit program
""")


def show_search_menu():
    """
    Display search menu to user
    """
    clear_screen()
    print("*"*25)
    print("Do you want to search by:")
    print("*"*25)
    print("""
a) Exact Date
b) Time Spent
c) Exact Search
d) Regex Pattern
e) Date Range
f) Return to menu
""")
