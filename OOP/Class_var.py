"""
    Difference between class variable and Instance variable
    Instance Variable:
        -The Instance variable is unique for each instance
        -If we changed the class variable for specific instance then it will create a new
         instance variable for that instance
    Class Variable:
        The class variable is shared among all instance of class 
        - cannot be changed by instance 
        - It is also known as static variable

    Note :
        1].__dict__ : It will return a dictionary that contains the attribute of instance
"""
class Student:
    branch = "Computer Engineering"

pratik = Student()
ajit = Student()
#For Pratik instance
pratik.name = "Pratik"  # This name is a instance variable of pratik
pratik.rollNum = 69     
#For Ajit intance
ajit.name = "Ajit"      # This name is instance variable of Ajit
ajit.rollNum = 50


print(f"The Name {pratik.name} and Roll number {pratik.rollNum} and branch is {pratik.branch}")
print(f"The Name {ajit.name} and Roll number {ajit.rollNum} and branch is {ajit.branch}")
print("All the instance variable of Pratik:",pratik.__dict__)
print("All the instance variable of ajit:",ajit.__dict__)

# If we have to change the branch for specific instance 
ajit.branch = "Civil Enginnering"
print("After changing the branch")
print(f"The Name {pratik.name} and Roll number {pratik.rollNum} and branch is {pratik.branch}")
print(f"The Name {ajit.name} and Roll number {ajit.rollNum} and branch is {ajit.branch}")

#If we change the branch of specific instance then it creates a new instance variable
# for that instance and it does not affect the class variable 
print("After chaging the class variable for specific instance:",ajit.__dict__)


#And We can access it by clas name
print("The class variable is:",Student.branch)