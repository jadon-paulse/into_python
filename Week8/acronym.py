
word_except = input("Enter word to be ignored separated by commas: ").split(", ")
title = input("Enter a title to generate its acronym: ").split()
# short = title.split()
acronym = [word[0] for word in title if word.lower() not in word_except]

print("The acronym is", ''.join(acronym))