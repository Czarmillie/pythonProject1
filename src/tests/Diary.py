from tests.Diary.Entry import Entry


class Diary:
    def __init__(self, user_name: str, password):
        self.user_name = user_name
        self.password = password
        self.is_locked = True
        self.entries = []
        self.number_of_entries = 0

    def get_user_name(self):
        return self.user_name

    def get_password(self):
        return self.password

    def unlock(self, password):
        if self.password == password:
            self.is_locked = False

    def lock(self):
        self.is_locked = True

    def is_locked(self):
        return self.is_locked

    def add_entry(self, title, body):
        new_entry = Entry(title, body)
        self.entries.append(new_entry)
        self.number_of_entries += 1

    def delete_entry(self, title, body):
        for entry in self.entries:
            if entry.get_entry_title() == title and entry.body == body:
                self.entries.remove(entry)
                self.number_of_entries -= 1

    def generate_id(self,):
        return self.number_of_entries + 1

    def find_entry_by_id(self, id):
        return self.entries.get(id, None)

    def update_entry(self, id, new_text):
        if id in self.entries:
            self.entries[id] = new_text
            return True
        else:
            return False