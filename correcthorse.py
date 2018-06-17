#!/usr/bin/python

# Import SystemRandom for secure cryptography
#from import random
from random import SystemRandom
import tkinter as tk

#Specify dictionary file
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

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.pw0 = tk.Button(self)
        self.pw0["text"] = password[0]
        self.pw0.pack(side="top")
        self.pw1 = tk.Button(self)
        self.pw1["text"] = password[1]
        self.pw1.pack(side="top")
        self.pw2 = tk.Button(self)
        self.pw2["text"] = password[2]
        self.pw2.pack(side="top")
        self.pw3 = tk.Button(self)
        self.pw3["text"] = password[3]
        self.pw3.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")
                       
        def regenPw():
            password = []
            password = genPassword(dictList, password)
            self.pw0["text"] = password[0]
            self.pw1["text"] = password[1]
            self.pw2["text"] = password[2]
            self.pw3["text"] = password[3]
            
        self.regen = tk.Button(self, text="REGEN PASSWORD", command=regenPw)
        self.regen.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
