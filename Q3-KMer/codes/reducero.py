#!/usr/bin/python3

from operator import itemgetter
import sys

wc = dict()
n = 9
for line in sys.stdin:
    line = line.strip()

    mer, count = line.split(' ', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if mer in wc:
        wc[mer]+=count
    else:
        if word:
            wc[mer] = count

sort_wc = sorted(wc, key = wc.get, reverse = True)

for r in sort_wc[:10]:
    print(r, wc[r])
