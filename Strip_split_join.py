# strip() method: This method removes the extra spaces from the left and right of string
string = "    1 2 3 4 5      "
string = string.strip()
print(string, type(string))

# split() : It splits the string into list element after breaking the given string by specified separator
string = "1_2_3_4_5"
string = string.split("_")
print(string) 

li = list(map(int, input("Enter the Number: ").split()))
print(li)

# join() It take all element in itearable and join them into the string
my_list = input()
my_list = "-".join(my_list)
print(my_list)
print(type(my_list))
