# Program Name: swordfish.py
# Program Description: Program runs and prints results based on name and password input
# Programmer Name: Taylor Bailey

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        print('Access granted.')
        for counter in range(65,91):
            print(end = str(chr(counter)))
    break
