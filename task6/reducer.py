#!/usr/bin/python2.7
# reducer.py
import sys

total_sum_of_votes =0.0;
total_sum_of_titles =0;

def reduce_function(line):
	global total_sum_of_titles,total_sum_of_votes
	curr_sum_of_titles,curr_sum_of_ratings=line.strip().split("\t")
	

	curr_sum_of_titles = int(curr_sum_of_titles.strip())
	curr_sum_of_ratings = float (curr_sum_of_ratings.strip())
	total_sum_of_votes += curr_sum_of_ratings
	total_sum_of_titles += curr_sum_of_titles 


for line in sys.stdin:
	reduce_function(line)

print round(total_sum_of_votes/total_sum_of_titles,2)
