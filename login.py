from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from database1 import DataBase1
from database2 import DataBase2
from kivy.uix.scrollview import ScrollView


class ExistingAccountWindow(Screen):
    student = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_btn(self):
        if self.student.text != "" and self.password.text != "":
            if db.validate(self.student.text, self.password.text):
                self.reset()
                sm.current = "view"
            elif db1.validate_uploaders(self.student.text, self.password.text):
                self.reset()
                sm.current = "upload"
            else:
                self.reset()
                invalid_login()
        else:
            self.reset()
            invalid_form()

    def reset(self):
        self.student.text = ""
        self.password.text = ""


class AdministratorWindow(Screen):
    namee1 = ObjectProperty(None)
    teachers = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit1(self):
        if db2.add_uploaded(self.teachers.text, self.password.text, self.namee1.text) != 1:
            sm.current = 'administrator'
            invalid_id()
            if self.namee1.text != "" and self.teachers.text != "":
                if self.password != "":
                    db1.add_uploaders(self.teachers.text, self.password.text, self.namee1.text)
                    self.reset()

                else:
                    invalid_login()

            else:
                invalid_form()

        else:
            sm.current = 'upload'

    def reset(self):
        self.teachers.text = ""
        self.password.text = ""
        self.namee1.text = ""


class FirstWindow(Screen):
    pass


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    student = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if db.add_user(self.student.text, self.password.text, self.namee.text) != 1:
            sm.current = 'create'
            invalid_id()
            if self.namee.text != "" and self.student.text != "":
                if self.password != "":
                    db.add_user(self.student.text, self.password.text, self.namee.text)
                    self.reset()

                else:
                    invalid_login()

            else:
                invalid_form()
        else:
            sm.current = 'view'

    def reset(self):
        self.student.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    student = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_btn(self):
        if self.student.text != "" and self.password.text != "":
            db.validate(self.student.text, self.password.text)
            self.reset()
            sm.current = "view"

        else:
            invalid_form()

    def create_btn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.student.text = ""
        self.password.text = ""


class UploadWindow(Screen):
    text = ObjectProperty(None)

    def to_upload_text(self):
        if self.text.text != 1:
            db2.add_uploaded(self.text.text)
        else:
            self.reset()
            sm.current = 'upload'

    def reset(self):
        self.text.text = ""


class ViewWindow(Screen):
    pass


class ScrollableLabel(ScrollView):
    pass


class WindowManager(ScreenManager):
    pass


def invalid_login():
    pop = Popup(title='Invalid Login', content=Label(text='Invalid username or password.'), size_hint=(None, None),
                size=(400, 400))
    pop.open()


def invalid_form():
    pop = Popup(title='Invalid Form', content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


def invalid_id():
    pop = Popup(title='Invalid ID', content=Label(text='ID ALREADY TAKEN'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


kv = Builder.load_file("lo.kv")

sm = WindowManager()
db = DataBase("users.txt")
db1 = DataBase1("uploaders.txt")
db2 = DataBase2("uploaded.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), UploadWindow(name="upload"),
           FirstWindow(name="First"), AdministratorWindow(name="administrator"), ExistingAccountWindow(name="existing"),
           ViewWindow(name="view")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "First"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    LOGIN_App = MyMainApp()
    LOGIN_App.run()
