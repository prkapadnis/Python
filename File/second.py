"""
    write() function:
        - The Write function writes the specified text into the file.
        - Where the specified text is inserted is depends on the file mode and stram position.
        - if 'a' is a file mode then it well be inserted at the stream position and default is 
          end of the file.
        - if 'w' is a file mode then it will override the file and insert it at the begining.
"""
with open("Python/File/my_data2.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some Random Text \nand more random text \nand more and more and more random text")

with open("Python/File/my_data2.txt", encoding="utf-8") as myFile:
    print(myFile.read())

print()

with open("Python/File/my_data2.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Name: pratik Rajendra Kapadnis")

with open("Python/File/my_data2.txt", encoding="utf-8") as myFile:
    print(myFile.read())
