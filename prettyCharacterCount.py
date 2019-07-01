#Program Name: prettyCharacterCount.py
#Program Description: Outputs a string in pretty print format
#Programmer's Name: Taylor Bailey

import pprint

while True:

    print('Enter a string: (blank to quit)')
    string = input()
    
    if string == "":
        print('Good Bye')
        break
    else:
        count = {}
        for character in string:
            count.setdefault(character, 0)
            count[character] = count[character] + 1
        pprint.pprint(count)
        break
