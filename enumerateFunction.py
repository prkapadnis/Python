"""
    enumerate()
        This function adds a counter to an iterable and returns it in the form of 
        (index, element)
"""
myList = ["zero", "first", "second", "third", "fourth", "fifth"]
for index, element in enumerate(myList):
    print(f"at {index} the value is {element}")
