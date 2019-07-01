# Program Name: vampire.py
# Program Description: Program asks for user's name and age and makes decisions
  # based on these variables 
# Programmer Name: Taylor Bailey

print('Hello! What is your name?')
name = input()
print('What is your age?')
age = (int(input()))

if age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
elif name == 'Alice':
    print('Hi Alice.')
else:
    print('You are not Alice.')
