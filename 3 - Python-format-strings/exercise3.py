# format() function's merge feature
medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = '{} - take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{medicine} - take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 160, duration = 6)
print(instructions)

# formatted string literals, or "f-strings"
name = 'World'
msg = f'Hello, {name}.'
print(msg)

count = 10
val = 3.14
msg = f'Count to {count}. Multiply by {val}'
print(msg)

# Stuff
width = 5
height  = 10
print(f'The perimeter is {(2 * width) + (2 * height)} and the area is {width * height}')

# Format specifiers to control alignment and padding
value = 'hi'
print(f'|{value:<25}|')
print(f'|{value:>25}|')
print(f'|{value:^25}|')
print(f'|{value:-^25}|')

