#Program Name: workWithFiles.py
#Program Description: Practice with reading and writing from a file
#Programmer's Name: Taylor Bailey

import os
print(os.getcwd())
os.chdir('C:\\cpt180Stuff')
print(os.getcwd())
if os.path.exists('C:\\cpt180Stuff\cellphones') == False:
    os.mkdir('cellphones')
print('The CPT180Stuff folder contains the following: ', end='')
print(os.listdir('C:\\cpt180Stuff'))
print('The CPT180Stuff\cars folder contains the following: ', end='')
print(os.listdir('C:\\cpt180Stuff\cars'))
print('The CPT180Stuff\pets folder contains the following: ', end='')
print(os.listdir('C:\\cpt180Stuff\pets'))
print('The C:\CPT180Stuff\pets\cats folder contains the following: ')
print('catnames.txt: ', end='')
print(os.path.getsize('C:\\cpt180Stuff\pets\cats\catnames.txt'), str('bytes'))
print('cats.jpg: ', end='')
print(os.path.getsize('C:\\cpt180Stuff\pets\cats\cats.jpg'), str('bytes'))
print('The C:\CPT180Stuff\pets\dogs folder contains the following: ')
print('dognames.txt: ', end='')
print(os.path.getsize('C:\\cpt180Stuff\pets\dogs\dognames.txt'), str('bytes'))
print('dogs.jpg: ', end='')
print(os.path.getsize('C:\\cpt180Stuff\pets\dogs\dogs.jpg'), str('bytes'))
