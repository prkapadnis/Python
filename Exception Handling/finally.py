"""
    finally: The finally blocks gets executed no matter what.
"""
try:
    num = int(input("Enter the a digit: "))
except ValueError:
    print("Enter the valid digit!")
finally:
    print("I executed no matter what!")