#!/usr/bin/python3

from operator import itemgetter
import sys

wc = dict()
t = "Total number of numeric cards"
wc[t] = 0
for line in sys.stdin:
    line = line.strip()
    wc[t]+=1
    suit, count = line.split(' ', 1)
    
    if not count.isdigit():
        continue

    if suit in wc:
        wc[suit]+=int(count)
    else:
        if suit:
            wc[suit] = int(count)

for r in wc:
    print(r, wc[r])
