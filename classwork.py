import re
import random
import string

def greet(name: str):       #anotation, recommend type of data
    print(f'hello {name}')

greet('test')

#password generator

def my_funct():
    pass    #let us make an empty function

def password_generator(password_len: int, include_punctuation = False):

    if password_len < 8 or password_len >30:
        return

    pattern = string.ascii_letters + string.digits
    if include_punctuation:
        pattern += string.punctuation

    password = ''
    for _ in range(password_len):
        password += random.choice(pattern)
    return password

#second option
    #return''.join(random.choice(pattern) for _ in range(password_len)) ///


print(password_generator(15, include_punctuation=True))

print(password_generator(10))



def multi(*numbers: int):
    result = 1
    for n in numbers:
        result *= n
    print(result)
    return result


multi(1,2,3,4,5)