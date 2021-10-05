class Student:                                                                   
    name = input("Enter the name:")
    rollNumber = int(input("Enter the Roll Number: "))      

    def display(self):
        print(f"The name is {self.name}")
        print(f"The Roll number is {self.rollNumber}")
        print(self.__class__) # It return the class name of current object

pratik = Student()
pratik.display()
Student.name = "Pratiksha"
pratik.name = "pratik"
print(pratik.name)
print(Student.name)