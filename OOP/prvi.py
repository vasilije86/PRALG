class User():
    def __init__(self, name):
        self.name = name
        print(self.name, "constructed")
    def who_am_i(self):
        print("I am", self.name)
    def login(self):
        print("Logged in as", self.name)

class Admin(User):
    def login_admin(self):
        print("Logged in as", self.name, "admin")

u1 = User('John')
u2 = Admin('Steve')

u1.who_am_i()   
u1.login()
u2.who_am_i()
u2.login_admin()

