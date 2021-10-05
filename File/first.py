"""
    reading and writing the file
"""
import os
# Writing into the file
with open("Python/File/my_data.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some Random Text \nand more random text \nand more and more and more random text")

# Reading the file and printing it
with open("Python/File/my_data.txt", encoding="utf-8") as my_file:
    print(my_file.read())

print(my_file.closed) #It will closed the file

#Appending the text into the file
with open("Python/File/my_data.txt", mode="a", encoding="utf-8") as my_file:
    my_file.write("\nmore and more and more and more random text!!!")

# printing It
with open("Python/File/my_data.txt", encoding="utf-8") as my_file:
    print(my_file.read())

