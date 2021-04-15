import datetime


class DataBase:
    def __init__(self, users):
        self.filename = users
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            student, password, name, created = line.strip().split(";")
            self.users[student] = (password, name, created)

        self.file.close()

    def get_user(self, student):
        if student in self.users:
            return self.users[student]
        else:
            return -1

    def add_user(self, student, password, name):
        if student.strip() not in self.users:
            self.users[student.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            return False

    def validate(self, student, password):
        if self.get_user(student) != -1:
            return self.users[student][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:

            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")
    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

