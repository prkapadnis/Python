"""
    There are various common procedures to read the file
        1]read() : It reads everything into one string
        2]readline() : This method reads the one line from the file.
        3]readines() : This method returns the list which contanis each line of the file as 
                        a list item.
"""
# read()
with open("Python/File/my_data.txt", encoding="utf-8") as myFile:
    print(myFile.read())

# readline()
with open("Python/File/my_data.txt", encoding="utf-8") as myFile:
    while True:
        line = myFile.readline()
        if not line:
            break
        print(line, end="")

# readlines()
with open("Python/File/my_data.txt", encoding="utf-8") as myFile:
    print(myFile.readlines())
