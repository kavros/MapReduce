#!/usr/bin/python2.7
# combiner.py
import sys

sum_of_votes=0;
sum_of_titles=0;

def combine_function(line):
	global sum_of_votes,sum_of_titles
	curr_total_titles,curr_sum_of_votes = line.strip().split("\t")
	
	curr_total_titles = int(curr_total_titles)
	curr_sum_of_votes = int(curr_sum_of_votes)

	sum_of_votes += curr_sum_of_votes
	sum_of_titles += curr_total_titles


for line in sys.stdin:
	combine_function(line)
print sum_of_titles,"\t",sum_of_votes