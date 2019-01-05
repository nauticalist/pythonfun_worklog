from task import Task
import utils
import json


class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def __repr__(self):
        return "User: {}".format(self.username)

    def add_task(self, date, title, time_spent, notes):
        task = Task(date, title, time_spent, notes)
        self.tasks.append(task)

    def to_json(self):
        return {
            'username': self.username,
            'tasks': [
                task.to_json() for task in self.tasks
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['username'])
        tasks = []
        for task_data in json_data['tasks']:
            tasks.append(Task.from_json(task_data))
        user.tasks = tasks

        return user

    @classmethod
    def create_or_get_user_from_file(cls):
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
        utils.clear_screen()
        print("Date of the task")
        date = utils.get_date()
        utils.clear_screen()
        title = input("Title of the task: ")
        utils.clear_screen()
        time_spent = input("Time spent(rounded minutes): ")
        utils.clear_screen()
        notes = input("Notes (Optional, you can leave this empty): ")
        self.add_task(date, title, time_spent, notes)
        with open("{}.json".format(self.username.lower()), 'w') as file:
            json.dump(self.to_json(), file, indent=4)

    def search_by_exact_date(self):
        utils.clear_screen()
        print("Enter the date")
        date = utils.get_date()
        return list(filter(lambda task: task.date == date, self.tasks))
