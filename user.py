from task import Task
import utils
import json
import re


class User:
    def __init__(self, username):
        """
        Let's set class attributes
        """
        self.username = username
        self.tasks = []

    def add_task(self, date, title, time_spent, notes):
        """
        Add task to users tasks
        """
        task = Task(date, title, time_spent, notes)
        self.tasks.append(task)

    def to_json(self):
        """
        convert user object to json
        """
        return {
            'username': self.username,
            'tasks': [
                task.to_json() for task in self.tasks
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        """
        get user object from json
        """
        user = User(json_data['username'])
        tasks = []
        for task_data in json_data['tasks']:
            tasks.append(Task.from_json(task_data))
        user.tasks = tasks

        return user

    @classmethod
    def create_or_get_user_from_file(cls):
        """
        Request username and create json file if not exits
        If file exists fetch data from json file
        """
        user_name = input("Enter your username: ")
        filename = "{}.json".format(user_name.lower())
        if utils.file_exists(filename):
            with open(filename, 'r') as file:
                json_data = json.load(file)
            user = User.from_json(json_data)
        else:
            user = User(user_name)

        return user

    def create_users_task(self):
        """
        Get user input and create users task
        """
        utils.clear_screen()
        print("Date of the task")
        date = utils.get_date()
        utils.clear_screen()
        title = input("Title of the task: ")
        utils.clear_screen()
        time_spent = utils.get_time_spent()
        utils.clear_screen()
        notes = input("Notes (Optional, you can leave this empty): ")
        utils.clear_screen()
        self.add_task(date, title, time_spent, notes)
        print("Task successfully logged.\n")

    def write_json_file(self):
        """
        write updated user object to json file
        """
        with open("{}.json".format(self.username.lower()), 'w') as file:
            json.dump(self.to_json(), file, indent=4)

    def search_by_date(self):
        """
        search users' tasks by date
        """
        utils.clear_screen()
        print("Enter the date:\n")
        date = utils.get_date()
        return list(filter(lambda task: task.date == date, self.tasks))

    def search_by_time_spent(self):
        """
        search users task by time spent
        """
        utils.clear_screen()
        print("Please enter time spent on task:\n")
        time_spent = utils.get_time_spent()
        return list(
            filter(lambda task: task.time_spent == time_spent, self.tasks))

    def search_by_keywords(self):
        """
        Search for task title and notes by keyword
        """
        utils.clear_screen()
        print("Please enter a keyword to search:\n")
        keyword = input("Keyword: ")
        return list(
            filter(
                lambda task:
                keyword in task.title or keyword in task.notes, self.tasks))

    def search_by_pattern(self):
        """
        Search for task title and notes by regular expression pattern
        """
        utils.clear_screen()
        print("Please enter raw regular expression pattern:\n")
        entry = input("Pattern: ")
        pattern = re.compile(r'{}'.format(entry), re.X | re.M)
        return list(
            filter(
                lambda task:
                pattern.search(task.title) or pattern.search(task.notes),
                self.tasks))
