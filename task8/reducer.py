#!/usr/bin/python2.7
# reducer.py
import sys

prev_tconst = None;
prev_release_decade = None
prev_avg_rating=None
for line in sys.stdin:
	tconst, value = line.strip().split("\t")

	tconst = tconst.strip()
	value  = value.strip()

	
	if(value.find(".") > 0 ):
		prev_avg_rating = float(value)
	else:
		prev_release_decade = int(value)

	if(prev_tconst != tconst):
		prev_tconst = tconst
	else:
		if(prev_tconst != None ):
			print prev_release_decade,"\t",prev_avg_rating
