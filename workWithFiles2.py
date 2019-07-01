#Program Name: workWithFiles2.py
#Program Description: Practice with opening, editing, printing, and closing a file
#Programmer's Name: Taylor Bailey

newfile = open('C:\\cpt180Stuff\pets\dogs\dognames.txt', 'r')
newfiletext = newfile.read()
print(newfiletext)
newfile.close()

newfile = open('C:\\cpt180Stuff\pets\cats\catnames.txt', 'r')
newfiletext = newfile.read()
print(newfiletext)
newfile.close()

newfile = open('C:\\cpt180Stuff\pets\cats\catnames.txt', 'a')
newfile.write('Hazel \n')
newfile.write('Samantha')
newfile.close()

newfile = open('C:\\cpt180Stuff\pets\cats\catnames.txt', 'r')
newfiletext = newfile.read()
print(newfiletext)
newfile.close()
