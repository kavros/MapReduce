#!/usr/bin/python2.7
# reducer.py
import sys
totalLines=0
totalWords=0

for line in sys.stdin:          # For ever line in the input from stdin    
    line = line.strip()         # Remove trailing characters
    currTotalLines, numOfWords = line.split("\t", 1)
    try:	
    	currTotalLines  = int(currTotalLines)
    	numOfWords      = int(numOfWords)
    	totalLines += currTotalLines;
    	totalWords += numOfWords
    except ValueError:
    	continue
    

print totalWords," ",totalLines