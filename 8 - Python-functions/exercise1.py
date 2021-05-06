# Add code to the code file to create 
# and call a small function

def say_hello():
    print('Hello World!')

say_hello()

# Update the code from the previous step 
# and add code to accept an input parameter
print()
def say_hello(name):
  print(f'Hello {name}!')

say_hello('Bob')

# Modify the function call to leave out the argument
print()
def say_hello(name='World'):
  print(f'Hello {name}!')

say_hello()
say_hello('Bob')

# Update the code example to include a 2nd optional input parameter
print()
def say_hello(name='World', greeting=None):
  if greeting == None:
    print(f'Hello {name}!')
  else:
    print(f'{greeting} {name}!')

say_hello()
say_hello('Bob')
say_hello(greeting='Howdy')
say_hello('Bob', 'Howdy')

print()
print(type(None))

# Comment out the code from the previous steps 
# and add a new function that returns a value
print()
def add_two_numbers(x, y):
    return x + y

add_two_numbers(4, 6)
result = add_two_numbers(5, 7)
print(result)

# Comment out the code from the previous steps 
# and add a new function that returns a list
print()
def create_deck():
  suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  deck = []

  for  suit in suits:
    for rank in ranks:
      deck.append(f'{rank} of {suit}')

  return deck

my_deck = create_deck()
print(len(my_deck))

# Comment out the code from the previous steps 
# and add a new function that demonstrates variable 
# scope in a function
"""
def some_function():
    value = 10

print(value)
"""
value = 1

def some_function():
    value = 10
    return value

print(value) # 1
# ~~~~~~~
value = 1

def some_function():
    value = 10
    return value

print(value)# 1
some_function()
print(value)# 1
