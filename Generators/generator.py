"""
    Generator: The Generator is used to create our own iterator. It is a special type of function
                which does not return the values it returns the iterator object with sequence of 
                values.
               In Generator the yield statement is used instead of return statement.
    Yield : Yield returns the value and pauses the execution of function while maintaning the
            internal states.
"""
# Generator
def generator():
    for i in range(1, 11):
        yield i*i

nums = generator()
for i in nums:
    print(i)
# we can also use for loop on generator object
for num in nums:
    print(num)

# second generator
def is_even():
    for i in range(1, 11):
        if i % 2 == 0:
            yield i

# even_nums = is_even()
# for num in even_nums:
#     print(num)

