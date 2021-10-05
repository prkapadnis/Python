"""
Line : 1
Number of words : 3
Average count of chars : 4,7
and so on
"""
with open("Python/File/my_data.txt", encoding="utf-8") as file:
    line_count = 1
    while True:
        line = file.readline()
        if not line:
            break
        print("Line :", line_count)
        word_count = 0
        word_list = line.split()
        print("Numberr of words : ", len(word_list))
        char_num = 0
        for word in word_list:
            for char in word:
                char_num += 1
        avg_char_count = char_num / len(word_list)
        print(f"Average count of chars : {avg_char_count}")
    file.close()