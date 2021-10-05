"""
    Crossword game
"""
name = input("Enter your Name:")
print(f"hello {name}! welcome to the Guessing game....")
print("You have given a name of fruit and you have to guess it!")
word = "apple"
guesses = ""
chances = 5

while chances > 0:
    won = True
    for ch in word:
        if ch in guesses:
            print(ch, end=" ")
        else:
            print("_", end=" ")
            won = False
    
    if won:
        print("You Won!!!")
        break
    
    guess = input("\n\nGuess any character:")
    
    guesses += guess
    if guess not in word:
        chances -= 1
    if chances == 0:
        print("You Lose!!")
        break


    
