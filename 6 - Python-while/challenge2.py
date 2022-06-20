# Write the code to implement an improved num guessing game
import random

# Method 1
count = 0
guess = 0
number = random.randint(1, 20)

print(f'Guess a number between 1 and 20')

while guess != number:
    count += 1
    guess = input(f'Enter guess #{count}: ')

    if guess.isnumeric() == True:
        guess = int(guess)

        if guess > number:
            print('Your guess is too high, try again')
        elif guess < number:
            print('Your guess is too low, try again')
    else:
        print('Numbers only, please!')
        continue
else:
    print(f'You guessed it in {count} tries!')

# Method 2
value = random.randint(1, 10)
count = 0
guess = 0
print('Guess a number between 1 and 10')

while guess != value:
    count += 1
    guess = input(f'Enter guess #{count}: ')

    if guess.isnumeric():
        guess = int(guess)
    else:
        print('Numbers only, please!')
        continue

    if guess > value:
        print('Your guess is too high, try again!')
    elif guess < value:
        print('Your guess is too low, try again!')

else:
    print(f'You guessed it in {count} tries!')
