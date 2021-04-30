# Create a list of values
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

print(colors)
print(type(colors))

sundry = ['John', 3.14, 7, False]
print(sundry)
print(type(sundry))

# Empty list
my_list = []

# Use an index to access individual elements
print(f'\n0-based indexing into the list... second item: {colors[1]}')
print(f'Last item of the list: {colors[-1]}')
print(f'Next to the last item of the list: {colors[-2]}')

# Create a slice
print('\nPrint a SLICE, starting at index 2 and excluding index 5:')
print(colors[2:5])
print(type(colors[2:5]))

print('\nPrint a slice, starting at index 0 to index 3:')
print(colors[:3])

print('\nPrint a slice, starting a index 4 to the end of the list:')
print(colors[4:])

print('\nPrint a slice, from the 4th from the end (but not the last item):')
print(colors[-4:-1])

# Reverse and sort list
colors.reverse()
print(colors)

colors.sort()
print(colors)

# Treat the list like a queue
print(f'\n{colors}')

color = colors.pop(0)
print('popped', color)

print(colors)

# Add and remove elements from a list
print(f'\nOld list be like: \n{colors}')

colors.append('black')
colors.append('white')

colors.remove('yellow')
colors.remove('orange')

print(f'\nNew list be like: \n{colors}')

# Combine a new list with an existing list
new_colors = ['lime', 'gray']
colors.extend(new_colors)
print(f'\n{colors}')

# Clear all items from a list
print(f'\nClear all items from a list: \n{colors}')
colors.clear()
print(f'{colors}')