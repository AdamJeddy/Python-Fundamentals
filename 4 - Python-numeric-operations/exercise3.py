# Mathematical operations
val1 = 5
val2 = 4

sum = val1 + val2
difference = val1 - val2
product = val1 * val2
quotient = val1 / val2
modulus = val1 % val2
exponent = val1 ** val2 

print('Sum: ' + str(sum))
print('Difference: ' + str(difference))
print('Product: ' + str(product))
print('Quotient: ' + str(quotient))
print('Modulus: ' + str(modulus))
print('Exponent: ' + str(exponent))

# Control the default order of operations
print(3 + 4 * 5)
print((3 + 4) * 5)

# investigate division more closely
val1 = 5
val2 = 4

quotient = val1 / val2

print(type(quotient))
print(quotient)

# code to convert a float into an int
pi = 3.14
print(type(pi))
print(int(pi))

uptime = 99.99
print(type(uptime))
print(int(uptime))

# code that rounds to a specific decimal place
first_value = round(7.654321, 2)
print(first_value)

second_value = round(9.87654, 3)
print(second_value)
