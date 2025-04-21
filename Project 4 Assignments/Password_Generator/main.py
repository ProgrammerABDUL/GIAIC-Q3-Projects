import random

print("Welcome to Password Generator\n")

chars = 'abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ!@#$%^&*().,?0123456789'

number = int(input("How many passwords do you want? "))
length = int(input("Input your password length: "))

print("\nHere are your passwords:")

for i in range(number):
    passwords = ''
    for i in range(length):
        passwords += random.choice(chars)
    print(passwords)