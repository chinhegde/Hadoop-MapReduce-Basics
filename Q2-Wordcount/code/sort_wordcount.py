file = open("wordcount.txt", "r")
wc = {}
with file as fh:
	for line in fh:
		(key, val) = line.split()
		wc[key] = int(val)

sorted_wc = [(k,v) for k,v in sorted(wc.items(), key = lambda item: item[1],reverse = True)]
# print(sorted_wc[:10])

for i,j in sorted_wc[:10]:
	print(i,' = ',j)
