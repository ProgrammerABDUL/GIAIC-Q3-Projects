import random

# Rules
# r > s = r,
# p > r = p,
# s > p = s,

def play():
    user = input("What's your choice? 'r' for Rock, 'p' for Paper, and 's' for Scissor ").lower()
    computer = random.choice(['r', 'p', 's'])

    print(f"\nYou selected: {user}\nComputer selected: {computer}")

    if computer == user:
        return '\nIt\'s a tie'
    
    if is_win(user, computer):
        return '\nYou won!'
    
    return '\nYou Lost!'

def is_win(player , opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    
print(play())