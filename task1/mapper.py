#!/usr/bin/python2.7
# mapper.py
import sys
wordCounter=0
lineCounter=0
def map_function(document):
	line = document.strip()
	words = line.split()
	yield 1, len(words);

for line in sys.stdin:
	for key,totalWords in map_function(line):
		try:
			wordCounter+=int(totalWords)
			lineCounter+=int(key)
		except ValueError:
			continue
print lineCounter, "\t",wordCounter