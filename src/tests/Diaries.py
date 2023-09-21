from diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username: str, password: str):
        new_diary = Diary(username, password)
        self.diaries.append(new_diary)

    def find_by_username(self, username: str) -> Diary:
        for diary in self.diaries:
            if diary.username == username:
                return diary
        return None

    def delete(self, username: str, password: str):
        diary_to_delete = self.find_by_username(username)
        if diary_to_delete and diary_to_delete.password == password:
            self.diaries.remove(diary_to_delete)
