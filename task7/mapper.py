#!/usr/bin/python2.7
# mapper.py
import sys

sum_of_writers = 0;
sum_of_titles = 0;
def map_function(line):
	global sum_of_titles,sum_of_writers
	columns = line.strip().split("\t");
	writers = columns[2].strip().split(",")
	areAnyWriters = False
	for writer in writers:
		if(writer != "\N"):
			sum_of_writers +=1
			areAnyWriters =True
	
	if(areAnyWriters == True):
		sum_of_titles+=1


for line in sys.stdin:
 	map_function(line)
print sum_of_writers,"\t",sum_of_titles
