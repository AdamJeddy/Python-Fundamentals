def print_args(*args):
    #for arg in args:
    #    print(f'arg = {arg}')
    print(args)
    print(type(args))

print_args('a')
print_args('a', 'b')
print_args('a', 'b', 'c')

# ~~~~~~~~~~~~~~
"""
print()

def print_keywords_args(**kwargs):
    third = kwargs.get('third', None)
    if third != None:
        print('third arg =', third)

print_keywords_args(first='a')
print_keywords_args(first='b', second='c')
print_keywords_args(first='d', second='e', third='f')
"""
# ~~~~~~~~~~~~~~
print()
def print_keywords_args(**kwargs):
    print('\n')
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f'{key} = {value}')

    third = kwargs.get('third', None)
    if third != None:
        print('third arg =', third)

print_keywords_args(first='a')
print_keywords_args(first='b', second='c')
print_keywords_args(first='d', second='e', third='f')