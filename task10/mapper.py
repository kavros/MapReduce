#!/usr/bin/python2.7
# mapper.py
import sys
from collections import defaultdict


for line in sys.stdin:
	columns =  line.strip().split("\t");
	if len(columns) == 6:	 	# name.basics.tsv
		nconst = columns[0]
		titles = columns[5]
		
		for tconst in titles.split(","):
			print tconst,"\t","1","\t",nconst
						
	else:					# title.basics.tsv
		tconst = columns[0]
		release_year = columns[5]

		if(release_year != "\\N"):
			release_year = int(release_year)
			if(release_year >= 2010 and release_year<= 2018):
				print tconst,"\t","0"
		