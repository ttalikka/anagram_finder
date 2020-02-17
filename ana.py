#!/usr/bin/env python3

# generic imports
import random
import time
import sys

# itertools import
from itertools import combinations,permutations

"""
ana.py
Finds anagrams of a word in a wordlist, also lists shorter permutations (Scrabble cheater)
Running without any parameters defaults to a random 8 character long word
Can be invoked with a word or with a word length
Try to keep it under 10 characters or get a supercomputer!
"""

# note the start time
startTime = int(round(time.time() * 1000))

# parse the wordlist into a list
# wordlist format should be a single word per line
with open("kotus-siivottu.txt","r") as f:
  wordList = f.read().splitlines()

# returns the contents of a list as a string
def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

# returns a random word used in the main program
def wordOfTheDay(length):
    # keeps running until a suitable word is found
    while True:
        randomWord = wordList[random.randrange(0,len(wordList))]
        if len(randomWord) == length:
            return(randomWord)

# check for arguments
try:
    string = str(sys.argv[1])
    # sets the passed string as the main word
    # unless passed an integer, then generates a random word of n length
    if string.isdigit():
        string = wordOfTheDay(int(string))
except:
    # if no arguments are passed, default to a random 8 letter word
    string = wordOfTheDay(8)

# create a list out of the characters in the word
characterList = list(string)
# create a list for all the possible words (length of the word or less)
possibleWords = []

# add words to the aforementioned list
for L in wordList:
    if len(L) <= len(string):
        possibleWords.append(L)

# convert the list to a set for faster searching
possibleWords_set = set(possibleWords)

# print some info
print("Word of the day: {}".format(string))
print("Wordlist length: {}".format(len(wordList)))
print("Possible words with this word length: {}".format(len(possibleWords)))

# create all 2-len(n) character combinations from the word
combinationList = set()
for L in range(2, len(characterList)+1):
    for subset in combinations(characterList,L):
        combinationList.add(subset)

# create all the possible permutations of the combinations
perms = set()
for L in combinationList:
    for i in permutations(listToString(L)):
        perms.add("".join(i))

# print some more info
print("Permutations of this word: {}".format(len(perms)))

# check the permutations against the list of possible words
anagrams = []
for L in perms:
    word = listToString(L)
    if word in possibleWords_set and word not in anagrams:
        anagrams.append(word)

# sort alphabetically and long to short
anagrams.sort()
anagrams.sort(key=len, reverse=True)

# print the results
print("-----\nFound a total of {} anagrams or permutations\nTop 10 results for this word: ".format(len(anagrams)))
for L in anagrams[:10]:
    print(L)

# we are done, print the total execution time
endTime = int(round(time.time() * 1000))
print("\nProgram completed in {}ms\n".format(endTime-startTime))

# let the user see more results if wanted (if there are any)
if len(anagrams) > 10:
    if input("Press enter to view the rest of the results or Ctrl-C (or q and enter) to quit\n") == "q":
        exit()
    for L in anagrams[10:]:
        print(L)
