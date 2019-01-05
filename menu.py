def show_main_menu():
    """
    Display main menu to user
    """
    print("*"*26)
    print("What would you like to do?")
    print("*"*26)
    print("""
a) Add new entry?
b) Search in existing entries
c) Quit program
""")


def show_search_menu():
    """
    Display search menu to user
    """
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
