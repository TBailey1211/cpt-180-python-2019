# Program Name: myFavoriteCars.py
# Program Description: This program outputs a list of information using tuples
# Programmer Name: Taylor Bailey


cars = (('1965', 'Pontiac', 'GTO', 'blue'),
('1969', 'Plymouth', 'Roadrunner', 'yellow'),
('2002', 'Chevrolet', 'Z-28 Camaro', 'black'))


for car in cars:
    print(car[0] + ' ' + car[3] + ' ' + car[1] + ' ' + car[2])
