#!/usr/bin/python2.7
# mapper.py
import sys

for line in sys.stdin:
	columns = line.strip().split("\t")
	if(len(columns) == 9): 	#title.basics.tsv
		release_year = columns[5]
		tconst 		 = columns[0]
		if(release_year != "\\N"):
			release_year = int(release_year)
			if(release_year >= 1900 and release_year <= 1999):
				release_year = int(release_year/10)*10 			# makes last digit zero
				print tconst,"\t",release_year					
	
	else:					#title.ratings.tsv
		tconst 		= columns[0]
		avg_rating	= columns[1]
		print tconst,"\t",avg_rating
