#Import the random module
#import random 
# now change random to an alias
import random as dice

#roll = random.randint(1, 10)
roll = dice.randint(1, 10)
print(f'You rolled {roll}.')
