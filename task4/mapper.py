#!/usr/bin/python2.7
# mapper.py
import sys


#is it better if implement a hash map
def map_function(line):
	global knownKeys
	columns=line.strip().split("\t")
	genres= columns[8].split(",")
	return genres
	
for line in sys.stdin:
	for genre in map_function(line):
		print genre
   