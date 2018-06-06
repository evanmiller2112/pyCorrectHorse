#!/usr/bin/python

# Import SystemRandom for secure cryptography
import random

# Specify dictionary file
# This dictionary file was taken from the following GitHub repo: https://github.com/first20hours/google-10000-english
dictionary="./wordlist"

# Specify number of words in password
numWords = 4

# Open dictionay file
dictObj = open(dictionary)

# Create dictionary list object
dictList = list(dictObj)

def genPassword(dlist, pwlist):
    for i in range(numWords):
        pwlist.append(random.choice(dlist))
    return pwlist

# Generate password
password = []
password = genPassword(dictList, password)

for i in password:
    print(i)
