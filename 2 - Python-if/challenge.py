import time

value = input('Do you want to continue ? > ')

if value == 'no' or value == 'n':
    print('Exiting')
elif value == 'yes' or value == 'y':
    print('Continuing ...')
    time.sleep(2)
    print('Complete!')
else:
    print('Please try again and respond with yes or no')

    