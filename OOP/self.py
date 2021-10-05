"""
    self
        self ia variable which is used to bind the instance of a class to the instance variable
        We have to explicitly declare it as a first parameter to access the instance variable 
        and methods 
"""
class Student:
    name = None
    rollNum = None

    def print_details(self):
        print(f"Roll Number {self.rollNum} Name {self.name}")
        print(self) #It prints the memory address of that object

pratik = Student()
ajit = Student()

pratik.name = "pratik"
pratik.rollNum = 69

ajit.name = "Ajit"
ajit.rollNum = 50

pratik.print_details()  #need not to pass the self it gets implicitly passed
ajit.print_details()