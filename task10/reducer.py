#!/usr/bin/python2.7
# mapper.py
import sys

prev_tconst=None


for line in sys.stdin:
	columns = line.strip().split("\t")
	

	if(len(columns) == 2):			#this  line contains a tconst that has been released between 2010 and 2018
		prev_tconst=columns[0].strip()		
	else:							#this line contains three values ttxxxxx 1 nmxxxxx 
		tconst = columns[0].strip()
		nconst = columns[2].strip()
		if (prev_tconst == tconst ):
			print nconst