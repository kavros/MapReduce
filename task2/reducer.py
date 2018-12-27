#!/usr/bin/python2.7
import sys

prev_word = None
value_total = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    word, value = line.split(" ", 1)
    value = int(value)

    # Remember that Hadoop sorts mapper output by key, and the reducer takes these keys sorted
    if prev_word == word:
        value_total += value
    else:
        if prev_word != None:  # Write result to stdout
            if(value_total > 5):
                print(prev_word+"\t"+str(value_total))
            
        value_total = value
        prev_word = word

if prev_word == word:  # Don't forget the last key/value pair
    if(value_total > 5):
        print(prev_word+"\t"+str(value_total))