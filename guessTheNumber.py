# Program Name: guessTheNumber.py
# Program Description: The program has the user guess a number using inputs
# Programmer Name: Taylor Bailey

# This is a guess the number game.

import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 7):
    while guessesTaken < 7:
        try:
            print('Take a guess.')
            guess = int(input())
            break
        except ValueError:
            print('Ensure to enter an integer!')
            
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
