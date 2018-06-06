#!/usr/bin/python

# Import SystemRandom for secure cryptography
#from import random
from random import SystemRandom

# Specify dictionary file
# This dictionary file was taken from the following GitHub repo: https://github.com/first20hours/google-10000-english
dictionary="./wordlist"

# Specify number of words in password
numWords = 4

# Open dictionay file
dictObj = open(dictionary)

# Create dictionary list object
dictList = list(dictObj)
dictLen = len(dictList)

# Generate password function
def genPassword(dlist, pwlist):
    for i in range(numWords):
        pwlist.append(dlist[SystemRandom().randrange(dictLen)])
    return pwlist

# Generate password
password = []
password = genPassword(dictList, password)

for i in password:
    print(i)
