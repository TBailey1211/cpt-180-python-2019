# Program Name: circle.py
# Program Description: This program will ask the user for their name
  # the color of a circle, and the circle's radius. It will then print
  # the name, circle color, and the circle's area.
# Programmer Name: Taylor Bailey

print('What is your name?')
myName = input()
print('What is the color of the circle?')
circleColor = input()
print('What is the radius of the circle?')
circleRadius = float(input())
circleArea = circleRadius * circleRadius * 3.1416
print('Hello ' + myName + ', the circle is ' + circleColor + ' and has an area of', round(circleArea, 1))
