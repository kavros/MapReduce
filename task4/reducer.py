#!/usr/bin/python2.7
import sys

prev_word = None

for line in sys.stdin:          # For ever line in the input from stdin
    word = line.strip()        # Remove trailing characters

    # Remember that Hadoop sorts mapper output by key, and the reducer takes these keys sorted
    if prev_word != word:
        if (prev_word != None and prev_word != "\\N" ):  # Write result to stdout
            print prev_word
            
        prev_word = word

if prev_word == word:  # Don't forget the last key/value pair
    if (prev_word != "\N" ):
        print prev_word