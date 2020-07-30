import random

def passwordGenerator():
    lowerChars = ['a', 'b', 'c', 'd', 'e']
    upperChars = ['A', 'B', 'C', 'D', 'E']

    specialchars = ['&', '!', '*']

    numericChars = ['1', '2', '3', '4', '5']

    password = random.choice(lowerChars) + random.choice(upperChars) + random.choice(specialchars) + random.choice(numericChars)

    password = password + password

    return password

print(passwordGenerator())