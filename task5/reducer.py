#!/usr/bin/python2.7
# reducer.py
import sys

max_year=0;
min_year=0;
are_years_initialized=False;

def reduce_function(line):
	global min_year,max_year,are_years_initialized
	curr_min_year,curr_max_year =  line.strip().split("\t")

	curr_min_year = int(curr_min_year)
	curr_max_year = int(curr_max_year)

	if(are_years_initialized == False):
		are_years_initialized = True
		max_year = int(curr_max_year)
		min_year = int(curr_min_year)
		return;

	if(max_year < curr_max_year):
		max_year = curr_max_year
	if(min_year > curr_min_year):
		min_year = curr_min_year


for line in sys.stdin:
	reduce_function(line)
print min_year,"\t",max_year