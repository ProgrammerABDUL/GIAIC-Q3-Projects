# Madlibs

# Game Title
print("✨ Madlibs Game 🎮")

# Description
print("This is a simple Mad Libs game where you input words to create a funny story! 🔥\n")

# How to Play
print("How to Play: 📝")
print("1. You will be prompted to enter various types of words (nouns, verbs, adjectives, etc.).\n2. After entering all the words, a story will be generated using your inputs.\n")
print("Let's start the game! 🚀\n")

# Formatting
bold_start = "\033[1m"
end = "\033[0m"

def Madlibs():
    # Get word inputs
    adjective1 = input("Enter an adjective (like happy, scary, blue) 👉 ")
    adjective2 = input("Enter another adjective 👉 ")
    noun1 = input("Enter a noun (person, place, or thing) 👉 ")
    noun2 = input("Enter another noun 👉 ")
    verb1 = input("Enter a verb (action word) 👉 ")
    verb2 = input("Enter another verb ending in 'ing' 👉 ")
    place = input("Enter a place 🗺️ ")
    food = input("Enter a food item 🍕 ")

    list = [adjective1, adjective2, noun1, noun2, verb1, verb2, place, food]
    print("\nYour words are:")
    for i in list:
        if i == adjective1:
            print(f"Adjective 1- {bold_start}{i}{end}")
        elif i == adjective2:
            print(f"Adjective 2- {bold_start}{i}{end}")
        elif i == noun1:
            print(f"Noun 1- {bold_start}{i}{end}")
        elif i == noun2:
            print(f"Noun 2- {bold_start}{i}{end}")
        elif i == verb1:
            print(f"Verb 1- {bold_start}{i}{end}")
        elif i == verb2:
            print(f"Verb 2- {bold_start}{i}{end}")
        elif i == place:
            print(f"Place- {bold_start}{i}{end}")
        elif i == food:
            print(f"Food Item- {bold_start}{i}{end}")

    # Story
    story = f"\n🎉 Here's your Story:\nOne {bold_start}{adjective1}{end} day, two friends were {bold_start}{verb1}{end} at the {bold_start}{place}{end}. Suddenly, they saw a {bold_start}{adjective2} {noun1}{end}! The {bold_start}{noun1}{end} started {bold_start}{verb2}{end} towards them. 'Stop disturbing my peace!' shouted the {bold_start}{noun1}{end}. As they tried to escape, the {bold_start}{noun1}{end} tripped over a {bold_start}{food}{end} and crashed into a {bold_start}{noun2}{end}. Everyone started laughing, and they all became great friends! 🤣"
    print(story)

Madlibs()