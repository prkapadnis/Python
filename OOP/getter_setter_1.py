"""
    Getter and setter to validate the data
"""
class RollerCoster:
    def __init__(self, name= "", age = 0):
        self.name = name
        self.age = age
    

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 20:
            print("Please childrens are not allowed. the age limit is 20!!")
        else:
            self.__age = value

    def showData(self):
        print(f"Name : {self.name} and Age : {self.age} ")

child1 = RollerCoster("Pratik", 23)
child1.name = "Pratik"
child1.age = 17
child1.showData()    