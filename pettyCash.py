#Program Name: pettyCash.py
#Program Description: Program prints the quantity of each item in a dictionary
#Programmer's Name: Taylor Bailey

change = {'penny': [.01,57], 'nickel': [.05,34], 'dime': [.1,42], 'quarter': [.25,19],
          'half dollar': [.5,3], 'one dollar bill': [1,24], 'five dollar bill': [5,7],
          'ten dollar bill': [10,5], 'twenty dollar bill': [20,3]}

def displayChange(change):
    totalCash = 0
    for key, value in change.items():
        print(str(value[1]) + ' ' + key)
        totalCash += value[0] * value[1]
    print("Total in petty cash: " + str(totalCash))
displayChange(change)

