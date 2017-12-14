# Simple Python 3.6 script intended to enumerate lines on a list, and make a selection based on the line,
# while also printing out the contents of the line as a string.
# written by @jonBaul, 2017

from random import randint
# Looks for the file in the same directory as this python script
filename = "snesgameslist.txt"
file = open(filename, "r")
games = file.readlines()
randomgame = randint(0, len(games))

print(games[randomgame])