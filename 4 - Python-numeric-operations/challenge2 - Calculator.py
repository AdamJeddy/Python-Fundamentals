# Build a simple calculator
# Solution 1
import sys


val1 = input('Enter your First number \n> ')
val2 = input('Enter your Second number \n> ')
if val1.isnumeric() == False or val2.isnumeric() == False:
    print("Input entered wasn't a number.")
    sys.exit()

operation = input('Enter your Operation \n> ')

if operation == '+':
    print(val1, '+', val2, '=', int(val1) + int(val2))
elif operation == '-':
    print(val1, '-', val2, '=' , int(val1) - int(val2))
elif operation == '*':
    print(val1, '*', val2, '=', int(val1) * int(val2))
elif operation == '/':
    print(val1, '/', val2, '=', int(val1) / int(val2))
elif operation == '%':
    print(val1, '%', val2, '=', int(val1) % int(val2))
elif operation == '**':
    print(val1, '**', val2, '=', int(val1) ** int(val2))
else:
    print('Incorrect operation entered')

# Solution 2 w/ better end result formatting
print('\n\nSimple calculator!')

first_number = input('First number? ')
second_number = input('Second number? ')
if first_number.isnumeric() == False or second_number.isnumeric() == False:
    print('Please input a number.')
    sys.exit()

operation = input('Operation? ')

first_number = int(first_number)
second_number = int(second_number)

result = 0
if operation == '+':
    result = first_number + second_number
    label = 'sum'
elif operation == '-':
    result = first_number - second_number
    label = 'difference'
elif operation == '*':
    result = first_number * second_number
    label = 'product'
elif operation == '/':
    result = first_number / second_number
    label = 'quotient'
elif operation == '**':
    result = first_number ** second_number
    label = 'exponent'
elif operation == '%':
    result = first_number % second_number
    label = 'modulus'
else:
    print('Operation not recognized.')
    sys.exit()

print(label + ' of ' + str(first_number) + ' ' + operation + ' ' + str(second_number) + ' equals ' + str(result))