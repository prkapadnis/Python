# #Lambda Function or Anonymous function
# addition = lambda x, y : x + y
# print(addition(2,3))
# subtraction = lambda x , y : x - y
# print(subtraction(2, 3))
# multiplication = lambda x , y : x * y
# print(multiplication(2,3))
# division = lambda x , y : x / y
# print(division(2,3))

# in  list
power = [lambda x : x ** 2, lambda x : x ** 3, lambda x : x ** 4]
for func in power:
    print(func(4))

# in dictionary
player = {"Cricket" : (lambda : print("Virat Kohli")), "Football": (lambda : print("Lionel Messi"))}

player["Cricket"]()
import random

key = random.choice(["Cricket", "Football"])
player[key]()