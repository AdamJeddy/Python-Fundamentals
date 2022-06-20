# isnumeric()
import sys


numeric_value = '7'
print(numeric_value.isnumeric())

string_value = 'Bob'
print(string_value.isnumeric())

# Get user input by using if & isnumeric()

val1 = input('First Number: ')

if val1.isnumeric() == False:
    print('Value is not a number.')
    sys.exit()

val2 = input('Second Number: ')

if val2.isnumeric() == False:
    print('Value is not a number.')
    sys.exit()

print('Sum:', str(int(val1) + int(val2)))


# Updated Code
val1 = input('First Number: ')
val2 = input('Second Number: ')

if val1.isnumeric() == False or val2.isnumeric() == False:
    print('Please enter numbers only.')
    sys.exit()

val1 = int(val1)
val2 = int(val2)

sum = val1 + val2
print('Sum: ' + str(sum))