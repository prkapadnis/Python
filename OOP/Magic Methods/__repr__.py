"""
    __repr__():It is used to return the machine representation of any user defined class.
"""
class Student:
    def __init__(self, name, rollNumber, address):
        self.name = name
        self.rollNum = rollNumber
        self.address = address
    
    # def __repr__(self):
    #     return f"{type(self).__name__}({self.name}, {self.rollNum}, {self.address})"

s1 = Student("Pratik", 69, "Nampur")
print(repr(s1))
# print(str(s1))