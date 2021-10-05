#--------1------------
def first(string):
    print(string) 
# first("hello")
second = first
second("hello")

#----------2------------
def inc(x):
    return x+1
def dec(x):
    return x-1

def operate(func, x):
    result = func(x)
    return result
print(operate(inc, 5))
print(operate(dec, 5))

# -----------------3----------------
def is_called():
    def is_returned():
        print("Hello")
    return is_returned
new = is_called()
new()