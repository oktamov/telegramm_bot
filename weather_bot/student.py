class Student:
    def __init__(self, chat_id, fullname):
        self.chat_id = chat_id
        self.fullname = fullname

    def get_attrs(self):
        return {
            "chat_id": self.chat_id,
            "fullname": self.fullname
        }