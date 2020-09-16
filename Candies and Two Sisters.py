n = int(input())
j = []
for i in range(n):
    k = int(input())
    if k % 2 == 0:
        j.append(int(k / 2) - 1)
    else:
        j.append(int(k / 2))

for i in range(n):
    print(j[i])
