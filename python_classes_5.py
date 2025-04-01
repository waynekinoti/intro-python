# inheritance
class Person:
    def __init__(self, name: str, age: int) :
        self.name = name.capitalize()
        if age > 100:
            raise Exception("Age cannot be greater than 100")
        self.age = age

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")



class Student(Person): # inherit everythimg
     def __init__(self, name: str, age: int, course:list, adm_number:str ) :
         super().__init__(name, age)
         self.course = course
         self.adm_number = adm_number

     def print_details(self):
         super().print_details()
         print("Course:", self.course)
         print("Adm_number:", self.adm_number)

s1=Student("John", 18, ["Maths","Geo"], "ADM100")
s1.print_details()