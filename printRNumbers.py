# Program Name: printRandomNumbers.psy
# Program Description: Program prints numbers randomly based on user inputs
# Programmer Name: Taylor Bailey

import random

print('Enter number of random numbers needed.')
number = (int(input()))
print('Enter the lower limit.')
lower = (int(input()))
print('Enter the upper limit.')
upper = (int(input()))

for value in range(number):
    value = random.randint(lower, upper)
    print(value)
