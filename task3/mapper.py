#!/usr/bin/python2.7
# mapper.py
import sys
totalActors=0  

def map_function(line):
	columns=line.strip().split("\t")
	if(columns[4].find("actor") != -1 or columns[4].find("actress") != -1 ):
		return 1
	return 0

for line in sys.stdin:
	totalActors += map_function(line)
print totalActors
   