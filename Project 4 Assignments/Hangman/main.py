import random
from words import words

def valid_word(words):
    word = random.choice(words)
    # Ensure the word doesn't contain spaces or hyphens
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def display_board(guessed_letters, word):
    """
    Display the current state of the word with guessed letters
    """
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    
    return display_word.strip()

def Hangman():
    word = valid_word(words)  # Get a valid word
    guessed_letters = []  # List to keep track of guessed letters
    attempts = 6  # Number of allowed incorrect guesses
    guessed_word = display_board(guessed_letters, word)  # Initial word display
    print(f"Welcome to Hangman!\nThe word has {len(word)} letters.")
    
    while attempts > 0:
        print(f"\n{guessed_word}")
        print(f"You have {attempts} attempts remaining.")
        guess = input("Guess a letter: ").upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You've already guessed {guess}. Try another letter.")
            continue
        
        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guess is in the word
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            attempts -= 1
            print(f"Oops! {guess} is not in the word.")
        
        # Update the guessed word display
        guessed_word = display_board(guessed_letters, word)
        
        # Check if the player has guessed the word
        if '_' not in guessed_word:
            print(f"Congratulations! You've guessed the word: {word}")
            break

    # If the player runs out of attempts, the game is over
    if attempts == 0:
        print(f"Game Over! The word was: {word}")

Hangman()