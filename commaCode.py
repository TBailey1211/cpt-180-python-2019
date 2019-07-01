# Program Name: commaCode.py
# Program Description: This program outputs newList using a loop
# Programmer Name: Taylor Bailey

foods = ['apples', 'bananas', 'tofu', 'cats']

def listItems(list):
    finalList = ""
    endOfList = list[-1]
    for list in list[:-1]:
        finalList += list + ", "
    print(finalList + "and " + endOfList)

newList = ['dog', 'cat', 'bird', 'tiger', 'lion', 'camel', 'horse']

listItems(newList)
