#Program Name: workWithFiles3.py
#Program Description: Continued practice with printing information from a file
#Programmer's Name: Taylor Bailey

import os
import shutil


for folderName, subfolders, filenames in os.walk('C:\\cpt180Stuff'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)


    print('')

shutil.move('C:\\cpt180Stuff', 'C:\\cpt180Stuff-2018')
print('CPT180Stuff Folder renamed to CPT180Stuff-2018.')

for folderName, subfolders, filenames in os.walk('C:\\cpt180Stuff-2018'):
    for filename in filenames:
        os.rename(os.path.join(folderName, filename), os.path.join(folderName, filename + '-2018'))


for folderName, subfolders, filenames in os.walk('C:\\cpt180Stuff-2018'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)


    print('')
