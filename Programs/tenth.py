"""
    Count the prime number
"""

def isPrime(num):
    flag = False
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag is True:
        return False
    return True

number = int(input("Enter the number:"))
for i in range(2, number):
    if isPrime(i) is True:
        print(i)

