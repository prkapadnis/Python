"""
    Constructor
        The Constructor is used to instantiating the object
        It initialise the data members at the time of object creation
        It gets automatically called when the object is created
"""
class Student:
    def __init__(self, name, roll_num):
        self.name = name
        self.roll_num = roll_num
    
    def printing_details(self):
        print(f"Name: {self.name} Roll Number: {self.roll_num}")

pratik = Student("Pratik", 69)
ajit = Student("Ajit", 50)
pratik.printing_details()
ajit.printing_details()