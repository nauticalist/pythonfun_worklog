import os
import datetime


def file_exists(filename):
    """
    Check if the users json file exists
    """
    return os.path.isfile(filename)


def clear_screen():
    """
    Clear screen for windows or others
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_date():
    """
    Check date format and return it in DD/MM/YYYY format (string)
    """
    date = None
    while not date:
        date_input = input("Please use DD/MM/YYYY: ")
        try:
            date = datetime.datetime.strptime(date_input, '%d/%m/%Y')
        except ValueError:
            print("That's not a valid date. Please try again.")
    return date.strftime('%d/%m/%Y')
