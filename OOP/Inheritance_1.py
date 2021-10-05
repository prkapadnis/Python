"""
    Multiple Inheritance
"""
class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        print(f"The Name is {self.name} salary is {self.salary} and the role is {self.role}")

class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game
    
    def print_details_player(self):
        print(f"The Player name is {self.name} and plays {self.game}")

class CoolProgrammer(Employee, Player):
    pass

ajit = Employee("Ajit", 15000, "CEO")
gaurav = Employee("Gaurav", 15000, "CAA")

akash = Player("Akash", ["Cricket", "Football"])

pratik = CoolProgrammer("Pratik", 25000, "Programmer")
pratik.print_details()
pratik.game = ["Cricket", "Football"]
pratik.print_details_player()
# pratik.print_details_player()
