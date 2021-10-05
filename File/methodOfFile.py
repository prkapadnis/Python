"""
    There are some predefined methods of the file Handling in the python
        1]closed : It returns True if the file is closed otherwise False
        2]name : It returns the Name of the file
        3]mode : It returns the file mode of the file
        4]readable : It returns True if if the file can be readable otherwise False
        5]writable : It returns True if the file can be writable otherwise False
"""
with open("Python/File/my_data.txt", mode="w", encoding="utf-8") as File:
    print(File.name)
    print(File.mode)
    print(File.closed)
    print(File.readable())
    print(File.writable())
File.close()