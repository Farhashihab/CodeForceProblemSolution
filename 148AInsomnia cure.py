k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

klist = []
Llist = []
mlist = []
nlist = []

for i in range(d+1):
    if i%k == 0:
        klist.append(i)
    elif i%l == 0:
        Llist.append(i)
    elif i%m == 0:
        mlist.append(i)
    elif i%n == 0:
        nlist.append(i)

print(len(klist)+len(Llist)+len(mlist)+len(nlist)-1)

