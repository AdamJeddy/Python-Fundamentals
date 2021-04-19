value = '8'

# if, elif and else
if value == '7':
    print('Value is 7')
elif value == '8':
    print('Value is 8')
elif value == '9':
    print('The value is 9')
else:
    print('Value is not 7')

# Overlapping Boolean expressions ~ Beware of them
if value < '8':
    print('The value is less than 8')
elif value < '7': #this will never execute
    print('The value is less than 7')
else:
    print('The value is greater than 8')

# Nested if code blocks
first_val = True
sec_val = '6'

if first_val:
    if sec_val == '6':
        print('Got here, in the nested if!')



print('Finished')