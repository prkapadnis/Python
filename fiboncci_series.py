def fiboncci_iterative(number):
    sum = 0
    n1 = 0
    n2 = 1
    print(n1, n2, end=" ")
    for i in range(number-1):
        sum = n1 + n2
        print(sum, end=" ")
        n1 = n2
        n2 = sum

def fibonacci_recursive(number):
    if number == 1:
        return 1
    if number == 2:
        return 1
    else :
        return fibonacci_recursive(number-1) + fibonacci_recursive(number - 2)

fiboncci_iterative(5); print()
print("The fibonacci_recursive() :",fibonacci_recursive(5))