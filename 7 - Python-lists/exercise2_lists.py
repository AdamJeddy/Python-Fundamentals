# Test a value for inclusion in a list
numbers = [1, 3, 5]

print(5 in numbers)
print(8 in numbers)

print(5 not in numbers)
print(8 not in numbers)

# Loop through the List
print()
cities = ["Chicago", "London", "Tokyo"]

for city in cities:
    print(city)


# Break out a for loop
print()
numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
numbers.sort()

for number in numbers:
    if number > 42:
        break
    print(number)

# Use an else statement
print()
import random
numbers = []

while len(numbers) < 5:
    numbers.append(random.randint(1, 100))

for number in numbers:
    print(number)

    if number > 90:
        print('Found at least one number greater than 90')
        break
    print('No numbers greater than 90')
print('Complete')

# Use a continue statement
print()
values = ["Laptop", 7, "Phone", 3, "DSLR", 5]
eqiupment = []

for value in values:
    if isinstance(value, str) == False:
        continue
    eqiupment.append(value)

print(eqiupment)

# Create nested for loops
print()
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

for  suit in suits:
  for rank in ranks:
    print(f'{rank} of {suit}')

# Choose randomly from a list
print()

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
selected_number = random.choice(numbers)
print(selected_number)

selected_numbers = random.choices(numbers, k=3)
print(selected_numbers)
