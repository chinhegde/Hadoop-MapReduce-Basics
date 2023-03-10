#!/usr/bin/python3
import sys

for line in sys.stdin:
    line = line.strip()
    line = list(line.split())
    for i in range(0,len(line)-1,2):
	 if line[i+1].isdigit(): print(line[i],line[i+1])
