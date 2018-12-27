#!/usr/bin/python2.7
# mapper.py
import sys

sum_of_votes =0;
sum_of_titles =0;
def map_function(line):
	global sum_of_votes,sum_of_titles
	columns = line.strip().split("\t");
	num_of_votes = int(columns[2]);
	sum_of_votes += num_of_votes; 
	sum_of_titles += 1;

for line in sys.stdin:
	map_function(line)
print sum_of_titles,"\t",sum_of_votes;
 
