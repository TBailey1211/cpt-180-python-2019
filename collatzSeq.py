# Program Name: collatzSeq.py
# Program Description: A program that outputs the Collatz Sequence
# Programmer Name: Taylor Bailey

while True:
    try:
        def collatz(number):

            if number % 2 == 0:
                print(number // 2)
                return number // 2
            elif number % 2 == 1:
                result = 3 * number + 1
                print(result)
                return result
        print("Enter an integer to obtain the Collatz Sequence.")
        n = input()
        while n != 1:
            n = collatz(int(n))
        break
    except ValueError:
        print('Ensure to enter an integer value.')




