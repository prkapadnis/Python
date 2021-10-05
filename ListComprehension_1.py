# Print the power of 2 for element in each list
print(list(map(lambda x : x * 2, range(1, 11))))
print([x * 2 for x in range(1,11)]) #List Comprehension

# Print the Odd number form the list
print(list(filter((lambda x : x % 2 != 0), range(1,11))))
print([x for x in range(1, 11) if x % 2 != 0])

# print the power of 2 that are multiple of 8
print([i ** 2 for i in range(50) if i % 8 == 0])

# multiplying of two list
print([x * y for x in range(1,6) for y in range(6, 11)])

# Print the multiple of 9 between 1 to 1000
import random
print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])