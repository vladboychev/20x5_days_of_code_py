import random

print("Welcome to the Number Guessing Game!")
game = True
while game:
    number = random.randint(1, 100)
    attempts = 10
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ")
    if difficulty == 'h':
        attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    while guess != number and attempts > 0:
        if guess > number:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1
        if attempts != 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Guess again: "))

    if guess == number:
        print(f"You got it right. {number} is the number I thought of.")
    else:
        print("You have no attempts left.")

    if input("Play again - 'Y' or 'N': ").lower() != "y":
        game = False
