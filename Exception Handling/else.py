"""
    else: The else bloack executed when the try boack does not raise any error
        - If the program has exceptions which are not handled then at that time the else block 
        does not executed.
"""
first, second = input("Enter the two values: ").split()
try:
    quotient = int(first) / int(second)
    print(quotient)
except ZeroDivisionError:
    print("You cannot divivde bye zero!!")
except ValueError:
    print("please enter the valid value")
else:
    print("Program does not have any error")