#!/usr/bin/python3
import sys
n = 9
for line in sys.stdin:
    line = line.strip()

    for i in range(len(line)-(n-1)):
        print(line[i:i+n]," 1")
