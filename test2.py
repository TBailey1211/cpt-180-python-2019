#try:
   # print('Input a number.')
#    number = (int(input()))
 #   print('Your number is ' + str(number))
#except ValueError:
 #   print('Error. Not a number!')

while True:
    try:
        print('Input a number.')
        number = (int(input()))
        print('Your number is ' + str(number))
        break
    except ValueError:
        print('Error. Not a number!')


while True:
    try:
        secretNumber = random.randint(1, 20)
        print('I am thinking of a number between 1 and 20.')

        # Ask the player to guess 6 times.

        for guessesTaken in range(1, 7):
            print('Take a guess.')
            guess = int(input())

            if guess < secretNumber:
                print('Your guess is too low.')
            elif guess > secretNumber:
                print('Your guess is too high.')
            else:
                break

        if guess == secretNumber:
            print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
            break
        else:
            print('Nope. The number I was thinking of was ' + str(secretNumber))
            break
    except ValueError:
         print('Ensure to enter an integer!')
