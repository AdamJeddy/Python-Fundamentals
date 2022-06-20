# Write program to convert temp from Fahrenheit to Celsius

import sys


fahrenheit = input('Input your F temp: ')
if fahrenheit.isnumeric() == False :
    print('Input is not a number.')
    sys.exit()

celsius = int((int(fahrenheit) - 32) * 5/9)
print('Your C temp is', celsius)
