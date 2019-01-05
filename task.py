class Task:
    def __init__(self, date, title, time_spent, notes=""):
        """
        set task class attributes
        """
        self.date = date
        self.title = title
        self.time_spent = time_spent
        self.notes = notes

    def __repr__(self):
        """
        representation of a task object
        """
        task = "Date: {}\nTitle: {}\nTime Spent: {}\nNotes: {}".format(
            self.date, self.title, self.time_spent, self.notes)
        return task

    def to_json(self):
        """
        convert task object to json
        """
        return {
            'date': self.date,
            'title': self.title,
            'time_spent': self.time_spent,
            'notes': self.notes
        }

    @classmethod
    def from_json(cls, json_data):
        """
        get task object from json
        """
        return Task(**json_data)

