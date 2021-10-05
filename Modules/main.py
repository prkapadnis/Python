import operation  # this way we can import complete module

# from operation import get_sum   #this way we can import only a single function from the module

# import operation as op  #this way we can give a specific name to the module to use in the code.

#addition
print(f"The addition is {operation.get_sum(2,4)}")
#subtraction
print(f"The subtraction is {operation.get_subtract(4, 2)}")
# Multiplication
print(f"The Multi[lication is {operation.get_multiplication(4,5,2)}")
# Division
print(f"The division is  {operation.get_division(4,2)}")
# floor division 
print(f"The Floor division is {operation.get_floor_division(6,3)}")
# Modulor
print(f"The modulor is {operation.get_modulo(6,4)}")