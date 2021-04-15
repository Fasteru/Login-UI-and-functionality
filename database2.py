import datetime


class DataBase2:
    def __init__(self, uploaded):
        self.filename = uploaded
        self.uploaded = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.uploaded = {}

        for line in self.file:
            name, teachers, password, created = line.strip().split(";")
            self.uploaded[name] = (teachers, password, created)

        self.file.close()

    def get_uploaded(self, name):
        if name in self.uploaded:
            return self.uploaded[name]
        else:
            return -1

    def add_uploaded(self, name, teachers, password):
        if name.strip() not in self.uploaded:
            self.uploaded[name.strip()] = (teachers.strip(), password.strip(), DataBase2.get_date())
            self.save()
            return 1
        else:
            return False

    def validate_uploaded(self, name, password, teachers):
        if self.get_uploaded(name) != -1:
            return self.uploaded[name][0] == password and self.uploaded[name][1] == teachers
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:

            for upload in self.uploaded:
                f.write(upload + ";" + self.uploaded[upload][0] + ";" + self.uploaded[upload][1] + ";" + self.uploaded[upload][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

