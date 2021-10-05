class Student:
    def __init__(self, name, rollNum):
        self.__name = name
        self.rollNum = rollNum
    
    @property
    def name(self):
        print("getter called!!")
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) < 10:
            self.__name = value
        else:
            print("Enter the name again")


    def display(self):
        print(f"The name is {self.__name}")
        print(f"The Roll Number is {self.rollNum}")
    
name = input("Enter the name: ")
rollNum = int(input("Enter the Roll number: "))
s1 = Student(name , rollNum)
s1.display()
# print(s1.name)