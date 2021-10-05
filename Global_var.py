var = 10
def func():
    global var # To access the global variable the global keyword is used
    var = 2
    print("In the func() ",var)
func() 
print("out of the func() ",var)
print(var)
