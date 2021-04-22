# 3 ways of using capitalize()
message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = 'third message'
print(message.capitalize())

# Modify the case of the string
message = 'hello world'
print(message.lower()) #all lower case
print(message.upper()) # all upper case

message = message.title() 
print(message) 
print(message.swapcase()) 


# Counts the no. of times 1 str is found in another
location = 'Mississippi'
print(location.count('s'))
print(len('how many characters in this string?')) # gives the length

# Inspect the contents of the str
message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'), '\n')

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))

# Pos of a str inside another str
message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))
print(message.find('t'))
print(message.find('T'))

# code that strips empty char's from left, right or both
message = '    middle    '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')


# Replace 1 str with another
message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)

# Justify a str
msg = 'howdy'
print(msg.rjust(20))
print(msg.rjust(20, '-'))
print(msg.ljust(20))
print(msg.ljust(20, '-'))
