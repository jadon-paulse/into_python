

def to_pig_latin(s):
    lst = ['sh', 'th', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
    # sentence = input('Enter english sentence: \n')
    sentence = s.split()
    for k in range(len(sentence)):
        i = sentence[k]
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            sentence[k] = i + 'way'
        elif t(i) in lst:
            sentence[k] = i[2:] + 'a' + i[:2] + 'ay'
        elif i.isalpha() == False:
            sentence[k] = i
        else:
            sentence[k] = i[1:] + 'a' + i[0] + 'ay'
    return (' '.join(sentence))


def t(str):
    return str[0] + str[1]

def to_english(s):
    sentence = s.split(" ")
    english = ""
    for word in sentence:
        if word[:len(word) - 4:-1] == 'yaw':
            english += word[:len(word) - 3] + " "
        else:
            noay = word[:len(word) - 2]
            firstconsonants = noay.split("a")[-1]
            consonantsremoved = noay[:len(noay) - (len(firstconsonants)+1)]
            english += firstconsonants + consonantsremoved + " "
    return english

# s = input("Enter Pig Latin: \n")

# print(toEnglish())

# if __name__ == "__main__":
#     x = to_pig_latin()
#     print(x)