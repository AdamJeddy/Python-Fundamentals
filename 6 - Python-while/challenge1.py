# Write the code to implement a number guessing game
import random
# Solution 1
count = 0
guess = 0
number = random.randint(1, 5)
print(f'this is the number: {number}')

while guess != number :
    count += 1
    guess = input('Guess a number between 1 and 5: ')

    if guess.strip() == '':
        continue

    if guess.isnumeric():
        guess = int(guess)
print(f'You guessed it in {count} tries!')


# Solution 2
value = random.randint(1, 5)
count = 0
guess = 0
while guess != value:
    count += 1
    guess = input('Guess a number between 1 and 5: ')
    if guess.isnumeric():
        guess = int(guess)
else:
    print(f'You guessed it in {count} tries!')