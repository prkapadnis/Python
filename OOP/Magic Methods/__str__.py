"""
    __str__(): It is used to return the printable string repreenatation on any user defined class
"""
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first = first_name
        self.last = last_name
        self.email = self.first +"."+ self.last + "@gamil.com"
        self.salary = salary

    def __str__(self) -> str:
        return f"Name = {self.first} {self.last} and email is = {self.email} and salary is {self.salary} "
    
emp = Employee("Pratik", "Rajendra", 35000)
print(emp)