#!/usr/bin/python2.7
# reducer.py
import sys

totalActors=0
for numberOfActors in sys.stdin:
	totalActors = totalActors+int(numberOfActors);
print(totalActors)