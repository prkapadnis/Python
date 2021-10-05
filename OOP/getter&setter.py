"""
    Getters and Setters
    Getters : This method is used to get the value of a property.
    Setter : This method is used to set the value of a property.
    Uses:
        - To avoid direct access of properties of a class
        - To add validation logic to getting and setting the values
        - To maintain the consistent interface in case the internal details changed 
"""
class Student:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print("Enter the name again!!")
        
    def display(self):
        print(f"The name is {self.name}")
s1 = Student("Pratik")
s1.display()
print(s1.name)
s1.name = "PrKapadnisR"
print(s1.name)