from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            value = randint(0, level)
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

while True:
    try:
        guess = int(input("Guess: "))
        if guess == value:
            print("Just right!")
            break
        if guess > value:
            print("Too large!")
        if guess < value:
            print("Too small!")
    except ValueError:
        print("Invalid input. Please enter an integer.")
