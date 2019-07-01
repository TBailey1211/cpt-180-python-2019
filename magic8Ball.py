# Program Name: magic8Ball.py
# Program Description: This program simulates a magic 8 ball with random responses
    # based on user input
# Programmer Name: Taylor Bailey

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain!'
    elif answerNumber == 2:
        return 'It is decidedly so!'
    elif answerNumber == 3:
        return 'Yes.'
    elif answerNumber == 4:
        return 'Reply hazy, try again.'
    elif answerNumber == 5:
        return 'Ask again later!'
    elif answerNumber == 6:
        return 'Concentrate and ask again!'
    elif answerNumber == 7:
        return 'No.'
    elif answerNumber == 8:
        return 'Outlook not so good.'
    elif answerNumber == 9:
        return 'Very doubtful!'

print('What is your name?')
myName = input()
print('What is your yes/no question?')
question = input()

r = random.randint(1, 10)
fortune = getAnswer(r)
print(myName + ", " + fortune)
