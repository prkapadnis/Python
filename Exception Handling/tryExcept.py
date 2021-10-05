"""
    Exception : 
        try:The try block contains block of code which may contains the error.
        except : The Except block where we can handle the error.
"""
while True:
    try:
        number = int(input("Enter the number: "))
        break
    except ValueError:
        print("Please Enter the valid Number!!")