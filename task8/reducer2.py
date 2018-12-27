#!/usr/bin/python2.7
# reducer2.py
import sys

prev_decate=None
prev_decate_sum=0
prev_decate_cnt=0

for line in sys.stdin:
	decade,average_rating =line.strip().split("\t");
	average_rating = float(average_rating)
	decade=decade.strip();
	
	if(decade == prev_decate):
		prev_decate_cnt +=1
		prev_decate_sum += average_rating
	else:
		if(prev_decate != None):
			final_avg_rating = prev_decate_sum/prev_decate_cnt
			print prev_decate,"\t",round(final_avg_rating,1)

		prev_decate = decade
		prev_decate_sum = average_rating
		prev_decate_cnt =1
if(prev_decate == decade):
	final_avg_rating = prev_decate_sum/prev_decate_cnt
	print prev_decate,"\t", round(final_avg_rating,1)


