class User:

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def Name(self):
        print("моё имя", self.name)

    def surName(self):
        print("моя фамилия", self.surname)

    def fullName(self):
        print("меня зовут", self.name, self.surname)









