"""
    Reverse a number
"""
number = int(input("Enter the number:"))
reverse = 0
if number < 0:
    number = number * (-1)
    while number != 0:
        remainder = number % 10
        reverse = reverse * 10 + remainder
        number = number // 10
    print(-reverse)
else :
    while number != 0:
        remainder = number % 10
        reverse = reverse * 10 + remainder
        number = number // 10
    print(-reverse)

print(2**31)