#!/usr/bin/python2.7
# mapper.py
import sys

min_year=0;
max_year=0;
are_values_initialized=False;

def map_function(line):
	global min_year,max_year,are_values_initialized
	year = line.strip().split("\t")[5]

	#initialize values the first time
	if( (are_values_initialized == False) and (year != "\N")):
		are_values_initialized=True;
		min_year = int(year)
		max_year = int(year)
		return;

	if(year != "\N"):
		year = int(year)
		if( year  > max_year ):
			max_year =year
		if(year < min_year):
			min_year = year
	
for line in sys.stdin:
	map_function(line)
print str(min_year),"\t",str(max_year)
   