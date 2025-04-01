from datetime import date, datetime


class Person:
    def __init__(self, name, dob, gender, disabled):
        self.name = name
        self.dob = dob  # "2007-01-19"
        self.gender = gender
        self.disabled = disabled

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Dob: {self.dob}")
        print(f"Gender: {self.gender}")
        if self.disabled:
            print("Disabled")
        else:
            print("Enabled")
        print("_______________")

    def get_age(self):
        current_date = datetime.today()
        date_birth = datetime.strptime(self.dob, "%d-%m-%Y")
        age = current_date - date_birth
        print("Age is ", age.days // 365)
        # print(f"Age is {age.days//365}")


p1 = Person("John", "19-01-2000", "Male", False)
p2 = Person("Agwambo", "22-01-1997", "Female", True)

p1.print_details()
p1.get_age()