from datetime import datetime

class Entry:
    def __init__(self, id, title, body=""):
        self.id = id
        self.title = title
        self.date_created = None
        self.body = body

    def get_entry_title(self):
        return self.title

    def add_entry_title(self, title):
        self.title = title

    def add_entry_date(self):
        self.date_created = datetime.now().strftime("%a, %m-%d-%Y %I:%M:%S %p")

    def get_entry_date(self):
        return self.date_created

    def get_entry_id(self):
        return self.id