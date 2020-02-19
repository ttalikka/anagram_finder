# anagram_finder
Finds anagrams and shorter permutations of a word

Defaults to a random 8 letter word found on the wordlist. You can also pass a custom word (or just a sequence of characters) or a length of a word as a parameter.

Usage:
```
./ana.py
./ana.py nakkivene
./ana.py 10
python3 ana.py
```

Try to keep the word length at 10 characters or less, as permutations are quite heavy to calculate.

The wordlist included is the *Institute for the Languages of Finland*'s modern Finnish wordlist, which can be found in its original form at http://kaino.kotus.fi/sanat/nykysuomi/. It has been modified into a simpler form by removing the inflection data and the homonym numbers included in the original wordlist, leaving only a cleartext, new line delimited list of Finnish words. The original wordlist is licensed using CC BY 3.0 which allows the modification of the original material and using it in a new context.
