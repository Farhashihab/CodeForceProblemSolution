fname = input("Enter file name: ")
fh = open(fname)
count = 0
time = dict()
for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        line = line[5]
        line = line.split(":")
        line = line[0]
        print(line)
    count += 1
print("There were",count,"lines in the file with From as the first word")