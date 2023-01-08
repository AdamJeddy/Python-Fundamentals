import time

value = input('Do you want to continue ? > ')

if value in ('no', 'n'):
    print('Exiting')
elif value in ('yes', 'y'):
    print('Continuing ...')
    time.sleep(2)
    print('Complete!')
else:
    print('Please try again and respond with yes or no')

