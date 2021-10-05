"""
    Single Inheritance
"""
class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def print_details(self):
        print(f"The Name is {self.name} salary is {self.salary} and the role is {self.role}")


class Programmer(Employee):
    def __init__(self, name, salary, role, language):
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language

    def print_details_programmer(self):
        print(f"The Programmer name is {self.name} salary is {self.salary} and fvrt language is {self.language}")
    
ajit = Employee("Ajit", 15000, "CEO")
pratik = Programmer("Pratik", 1500000, "Programmer", ["Python", "C++"])

ajit.print_details()
pratik.print_details_programmer()
