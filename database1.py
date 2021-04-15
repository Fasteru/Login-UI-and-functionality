import datetime


class DataBase1:
    def __init__(self, uploaders):
        self.filename = uploaders
        self.uploaders = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.uploaders = {}

        for line in self.file:
            name, teachers, password, created = line.strip().split(";")
            self.uploaders[name] = (teachers, password, created)

        self.file.close()

    def get_uploaders(self, name):
        if name in self.uploaders:
            return self.uploaders[name]
        else:
            return -1

    def add_uploaders(self, name, teachers, password):
        if name.strip() not in self.uploaders:
            self.uploaders[name.strip()] = (teachers.strip(), password.strip(), DataBase1.get_date())
            self.save()
            return 1
        else:
            return False

    def validate_uploaders(self, name, password):
        if self.get_uploaders(name) != -1:
            return self.uploaders[name][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:

            for upload in self.uploaders:
                f.write(upload + ";" + self.uploaders[upload][0] + ";" + self.uploaders[upload][1] + ";" + self.uploaders[upload][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]