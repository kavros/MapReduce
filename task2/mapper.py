#!/usr/bin/python2.7
# mapper.py
import sys
 
def map_function(document):
    # Split doucment by words and use word as the key
    words = document.strip().split()
    bigram=dict();
    for i in range(0,len(words)-1):                   
        yield ((words[i]+"_"+words[i+1]), 1)
    
 
for line in sys.stdin:
    # Call map_function for each line in the input
    for key, value in map_function(line):
        # Emit key-value pairs using '\t' as a delimeter  
        print(key + " " + str(value))