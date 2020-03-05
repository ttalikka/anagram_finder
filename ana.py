#!/usr/bin/env python3

# generic imports
import random
import time
import sys
import io

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
with io.open("kotus-siivottu.txt",mode="r",encoding="utf-8") as f:
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
    # if no arguments are passed, default to a random 8-20 letter word
    string = wordOfTheDay(random.randrange(8,20))

# check for mode select, coming later, this is pretty placeholder stuff now
try:
    mode = str(sys.argv[2])
except:
    mode = ""

if mode == "sentence":
    print("whoo!")
    quit()

# create a list out of the characters in the word
characterList = list(string)
# create a list for all the possible words (length of the word or less)
possibleWords = set()
possibleWords_sorted = set()

# add words to the aforementioned list
for L in wordList:
    if len(L) <= len(string):
        possibleWords.add(L)
        possibleWords_sorted.add(tuple(sorted(L)))

# print some info
print("Word of the day: {}".format(string))
print("Wordlist length: {}".format(len(wordList)))
print("Possible words with this word length: {}".format(len(possibleWords)))
print("Unique sorted sequences with this word length: {}".format(len(possibleWords_sorted)))

# create all 2-len(n) character combinations from the word and save those which can be found in the sorted wordlist
combinationList = set()
for L in range(2, len(characterList)+1):
    for subset in combinations(characterList,L):
        if tuple(sorted(subset)) in possibleWords_sorted:
            combinationList.add(tuple(sorted(subset)))

# check the possible words sorted letter sequences against the sorted letter sequences available from the letters in the seed word
# if it's a match, it's an anagram, so add it to the list of anagrams
permutations = []
for L in possibleWords:
    if tuple(sorted(L)) in combinationList:
        permutations.append(L)

# sort alphabetically and long to short and remove the original word
permutations.sort()
permutations.sort(key=len, reverse=True)

if string in permutations:
    permutations.remove(string)

anagrams = []
for L in permutations:
    if len(L) == len(string):
        anagrams.append(L)
        permutations.remove(L)

# print the results
print("-----\nFound a total of {} anagrams and {} shorter permutations".format(len(anagrams),len(permutations)))
if len(anagrams) > 0:
    print("Anagrams:")
    for L in anagrams:
        print(L)
print("Top 10 permutations for this word:")
for L in permutations[:10]:
    print(L)

# we are done, print the total execution time
endTime = int(round(time.time() * 1000))
print("\nProgram completed in {}ms\n".format(endTime-startTime))

# let the user see more results if wanted (if there are any)
if len(permutations) > 10:
    if input("Press enter to view the rest of the results or Ctrl-C (or q and enter) to quit\n") == "q":
        exit()
    for L in permutations[10:]:
        print(L)
