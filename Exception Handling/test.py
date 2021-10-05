try:
    file = open("Python/Exception Handling/myData1.txt", encoding="utf-8")
except FileNotFoundError as ex:
    print("The file is not found!!")
    print(ex)
else:
    while True:
        line = file.readline()
        if not line:
            break
        print(line, end="")
    file.close()
finally:
    print("Finished working with file!!")