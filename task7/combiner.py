#!/usr/bin/python2.7
# mapper.py
import sys

sum_of_writers = 0;
sum_of_titles = 0;
def map_function(line):
	global sum_of_titles,sum_of_writers
	curr_num_of_writers,curr_num_of_titles = line.strip().split("\t");
	curr_num_of_titles = int(curr_num_of_titles)
	curr_num_of_writers = int(curr_num_of_writers)

	sum_of_titles += curr_num_of_titles
	sum_of_writers += curr_num_of_writers

for line in sys.stdin:
	map_function(line)
print sum_of_writers,"\t",sum_of_titles	