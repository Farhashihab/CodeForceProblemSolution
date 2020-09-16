fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        line = line[5]
        line = line.split(":")
        lst.append(line[0])
counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

for k,v in sorted(counts.items()):
    print(k,v)
