#!/usr/bin/env python3

# generic imports
import random
import time
import sys
import io
import argparse
from os import system, name 

# itertools import
from itertools import combinations

"""
ana.py
Finds anagrams of a word in a wordlist, also lists shorter permutations (Scrabble cheater)
Running without any parameters defaults to a random 8-20 character long word
Can be invoked with a word or with a word length
Try to keep it under 24 characters or get a supercomputer!
"""

"""
Definitions:
"""
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

def getAnagrams(string):

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

    # remove the anagrams from the list of shorter permutations
    anagrams = []
    for L in permutations:
        if len(L) == len(string):
            anagrams.append(L)
            permutations.remove(L)

    return anagrams, permutations

def clear(): 
    # clear screen function from https://www.geeksforgeeks.org/clear-screen-python/
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

"""
Main:
"""

clear()
parser = argparse.ArgumentParser(description='Create anagrams and permutations')
parser.add_argument("-l", "--length", type=int, help="Allows you to input a custom word length (default 8-20 characters)")
parser.add_argument("-w","--word", type=str, help="Allows you to input a custom word")
parser.add_argument("--wordlist", type=str, help="Allows you to use a custom wordlist")
args = parser.parse_args()

# note the start time
startTime = int(round(time.time() * 1000))

if args.wordlist:
    try:
        wordlist = args.wordlist
    except:
        print("Wordlist not found! Defaulting to the KOTUS wordlist...")
        wordlist = "kotus-siivottu.txt"
else:
    wordlist = "kotus-siivottu.txt"

# parse the wordlist into a list
# wordlist format should be a single word per line
with io.open(wordlist,mode="r",encoding="utf-8") as f:
  wordList = f.read().splitlines()

# check for arguments

# sets the passed string as the main word
# if no arguments are passed, default to a random 8-20 letter word
if args.word:
    if args.word.isdigit():
        print("Did you mean --length INT?")
        quit()
    string = args.word
else:
    string = wordOfTheDay(random.randrange(8,20))

# get a random word with a set length instead if length is supplied
if args.length:
    string = wordOfTheDay(int(args.length))

anagrams, permutations = getAnagrams(string)

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
print("\nProgram completed in {}ms\n".format(int(round(time.time() * 1000))-startTime))

# let the user see more results if wanted (if there are any)
if len(permutations) > 10:
    if input("Press enter to view the rest of the results or Ctrl-C (or q and enter) to quit\n") == "q":
        exit()
    for L in permutations[10:]:
        print(L)
