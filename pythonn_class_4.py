from datetime import date, datetime


class Car:
    def __init__(self, make, model, date_of_make, drive_side):
        self.make = make
        self.model = model
        self.date_of_make = date_of_make
        self.drive_side = drive_side

    def print_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Date of make: {self.date_of_make}")
        if self.drive_side:
            print(f"Left: {self.drive_side}")
        else:
            print(f"Right: {self.drive_side}")
        print("___________")

    def get_age(self):
        current_year = datetime.today().year
        date_of_make = datetime.strptime(self.date_of_make, "%d-%m-%Y")
        age = current_year - date_of_make.year
        print(f"Age is: {age}")


car1 = Car("Ford", "Mustang", "12-5-1998" , "Left" )
car2 = Car("Ford", "Mustang", "12-5-2008", "Right" )
car1.print_details()
car2.print_details()

