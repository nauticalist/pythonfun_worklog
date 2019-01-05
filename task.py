class Task:
    def __init__(self, date, title, time_spent, notes=""):
        self.date = date
        self.title = title
        self.time_spent = time_spent
        self.notes = notes

    def __repr__(self):
        task = "Date: {}\nTitle: {}\nTime Spent: {}\nNotes: {}".format(
            self.date, self.title, self.time_spent, self.notes)
        return task

    def to_json(self):
        return {
            'date': self.date,
            'title': self.title,
            'time_spent': self.time_spent,
            'notes': self.notes
        }

    @classmethod
    def from_json(cls, json_data):
        return Task(**json_data)

