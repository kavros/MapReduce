#!/usr/bin/python2.7
# reducer.py
import sys

sum_of_writers = 0;
sum_of_titles = 0;
def reduce_function(line):
	global sum_of_writers,sum_of_titles
	curr_sum_of_writers,curr_sum_of_titles = line.strip().split("\t")

	curr_sum_of_titles = int(curr_sum_of_titles)
	curr_sum_of_writers = int(curr_sum_of_writers)

	sum_of_writers +=curr_sum_of_writers
	sum_of_titles += curr_sum_of_titles


for line in sys.stdin:
 	reduce_function(line)
sum_of_writers = float(sum_of_writers)
sum_of_titles = float(sum_of_titles)
print int(round(sum_of_writers/sum_of_titles))
