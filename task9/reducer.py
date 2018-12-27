#!/usr/bin/python2.7
# reducer.py
import sys

prev_genre = None
value_total = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    word, value = line.split("\t")
    value = int(value)

    # Remember that Hadoop sorts mapper output by key, and the reducer takes these keys sorted
    if prev_genre == word:
        value_total += value
    else:
        if prev_genre != None:  # Write result to stdout
            print("{0}\t{1}".format(prev_genre, value_total))
            
        value_total = value
        prev_genre = word

if prev_genre == word:  # Don't forget the last key/value pair
    print("{0}\t{1}".format(prev_genre, value_total))
