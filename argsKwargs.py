def arguments(first, second, *args):
    sum = 0
    sum += first + second
    for i in args:
        sum += i
    return sum


print(arguments(32, 34, 67, 53, 58, 10))

def details(food, liquid, **kwargs):
    print(f"I love {food} food")
    print(f"I love {liquid} liquid")
    for key, value in kwargs.items():
        print(f"I love {value} as {key}")

details(food = "Chiken Lolipop", liquid = "Slice", Hobby = "Programming", FvrtLang = "Python")

