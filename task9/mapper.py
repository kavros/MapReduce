#!/usr/bin/python2.7
# mapper.py
import sys

from collections import defaultdict

genre_dict = defaultdict(int)
MAX_SIZE = 100

def map_function(line):
	columns=line.strip().split("\t")
	start_year = columns[5]	
	if( start_year != "\\N"):
		start_year = int(start_year)
		if(start_year >= 2000 and start_year <= 2014):
			genres = columns[8].split(",")
			for genre in genres:
				if(genre != "\\N"):
					yield genre,1
	

for line in sys.stdin:
 	for key,value in map_function(line):
 		genre_dict[key] += value

 		if len(genre_dict) > MAX_SIZE:
 			for key,value in genre_dict.items():
 				print(key + "\t" + str(value))
 			genre_dict.clear()

for key, value in genre_dict.items():     
    print(key + "\t" + str(value)) 
