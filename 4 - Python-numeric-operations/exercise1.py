# type() function
print(type('7'))
print(type(7))
print(type(7.1))

# isinstance() function
print(isinstance('7', str))     #true
print(isinstance(7, int))       #true
print(isinstance(7.1, float))   #true

print(isinstance(7, str))       #false
print(isinstance('7', int))     #false
print(isinstance('7.1', float)) #false

# type() used like isinstance()
print(type('7') == str)
print(type(7) == int)
print(type(7.1) == float)

print(type(7) == str)
print(type('7') == int)
print(type('7.1') == float)

# Variable can point to anything
x = 'a string'
print(type(x))
x = 7
print(type(x))
x = False 
print(type(x))
