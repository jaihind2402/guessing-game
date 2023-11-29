#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import guess_number_logo
print(guess_number_logo)
print("Welcome to the guessing game between 1 to 100")
comp_number = random.randint(1, 100)
print(f"computer chosen number is {comp_number} ")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
lives = 0
if difficulty == 'easy':
    lives = 10
else:
    lives = 5

should_continue = True
while should_continue:
    print(f'You have {lives} attempts remaining to guess the number')
    guess = int(input('Make a guess: '))
    if comp_number == guess:
        print(f'You got it! The answer was {guess}.')
        should_continue= False
    elif guess < comp_number:
        print('Too Low')
    else :
        print('Too High')
    lives-=1
    if lives == 0:
        should_continue = False