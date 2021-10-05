"""
    class Method
        The class method is a method which bound to the class rather than its object
        - The class method is used to modify the class variable
        - To called the class method doesn't required class instance
        - The class method is called by both by class or by object of that class
"""
class Student:
    leaves = 0

    def __init__(self, name, roll_num):
        self.name = name
        self.roll_num = roll_num

    def printing_detalis(self):
        print(f"Name is {self.name} and Roll Number is {self.roll_num} and Number of leaves {self.leaves}")

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.leaves = new_leaves
        print(cls)  # It prints the class name

pratik = Student("Pratik", 69)
ajit = Student("Ajit", 50)

pratik.change_leaves(1)     #It will also changed the class variable leaves
pratik.printing_detalis()
print(Student.leaves)