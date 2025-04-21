# Guess the Number Game

import random
import time

# User Role
def user(x):
    """User will guess the secret number between 1 to 100"""

    How_to_play = f"""How to play:
1. The computer will randomly select a number between 1 to {x}.
2. You will have 5 attempts to guess the number.
3. After each guess, the computer will tell you if your guess is too high or too low.
4. Try to guess the number in as few attempts as possible!

Good luck! 👍🏻. Let's start! 🚀"""
    print(How_to_play)
    time.sleep(1)

    random_number = random.randint(1, x)
    # print(random_number)
    user_guess = 0
    attempts = 5
    
    while user_guess != random_number and attempts > 0:
        user_guess = int(input("\nGuess the number: "))
        attempts -=1
        if user_guess > random_number:
            print(f"Too High 📈! You've {attempts} attempts left.")
        elif user_guess < random_number:
            print(f"Too Low 📉! You've {attempts} attempts left.")

    # Game Result
    if user_guess == random_number:
        no_of_attempts = 5
        attempts = no_of_attempts - attempts
        print(f"You won 🎉! You guessed a number {random_number} in {attempts} attempts")
    elif user_guess!= random_number:
        print(f"\nYou lost 😢! The number was {random_number}")

# Computer Role
def computer():
    """Computer will guess the secret number between 1 to 100"""

    range = int(input("What will be a second number in range. Range: 1 to ??: "))

    How_to_Play = f"""\nHow to play:
1. Pick a number from 1 to {range}, Keep it secret.
2. After each guess, you will be asked that Did user guess too high or too low.
3. If user guess your secret number by any chance, the msg will let you know that user guessed your number correctly!

Good luck! 👍🏻. Let's start! 🚀\n"""
    print(How_to_Play)
    time.sleep(2)

    low = 1
    high = range
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)?? \n").lower()

        if feedback == 'h':
            high = guess + 1
        elif feedback == 'l':
            low = guess - 1

    print(f"\nUser has guessed your number {guess} correctly!")

# Game Title
print("Geuss the Number!\n")

# Description
print("In this game, the user/computer will have a secret number between 1 to 100. The other have to guess it, Sounds Amazing?? Let's play 🎮!!\n")

# How to play
How_to_play = """How to play:
1. There are two roles 
    i) Computer 🤖
    ii) User 👤.
2. Select any, and take your game to the next level 🔥.

Let's start! ✨\n"""
print(How_to_play)

# Game Roles
role = str(input("Choose a Role:\n1. Play as a Computer(C)\n2. Play as a User(U)\nChoose any: ")).lower()

if role == 'c':
  print("\nHey! You selected Computer, Let's begin!")
  computer()
elif role == 'u':
  print("\nHey! You selected User, Let's begin!\n")
  user(100)
else:
    print("Invalid Input!")