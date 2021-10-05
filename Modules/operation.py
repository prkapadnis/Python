def get_sum(*args):
    total = 0
    for i in args:
        total += i
    return total

def get_subtract(first, second):
    return first - second

def get_multiplication(*args):
    total = 1
    for i in args:
        total *= i
    return total

def get_division(first, second):
    return first / second

def get_floor_division(first, second):
    return first // second

def get_modulo(first, second):
    return first % second