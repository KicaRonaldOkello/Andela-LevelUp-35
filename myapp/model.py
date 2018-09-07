from myapp import app

class Person:
    def __init__(self, name, age, sex):
        self.age = age
        self.sex = sex
        self.name = name

    def get_age(self):
        return "{} is having the age of {} ".format(self.name, self.age)

    def get_sex(self):
        return "{} is the sex of {} ".format(self.sex, self.name)

class User(Person):
    def __init__(self, name, age, sex, email):
        super().__init__(name, age, sex)
        self.email = email

    USERS = []
        
    def adding_user(self, data):
        data["id"] = len(self.USERS) + 1
        self.USERS.append(data)
        return self.USERS

    def getting_user(self):
        return self.USERS

    def deleting_user(self):
        removed_user = self.USERS[-1]
        self.USERS.remove(removed_user)
        return removed_user


class GuestList:

    GUESTS = []

    def adding_guest(self, guest_detail):
        self.GUESTS.append(guest_detail)
        return self.GUESTS

    def getting_guests(self):
        return self.GUESTS

    def deleting_guest(self, guest_no):
        removed = self.GUESTS[guest_no]
        self.GUESTS.remove(guest_no)
        return removed

