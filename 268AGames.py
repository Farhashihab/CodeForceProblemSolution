n = int(input())

b = []
c = []
for i in range(n):
    k = input().split()
    b.append(k[0])
    c.append(k[1])
sum = 0

for i in range(n):
    for j in range(n):
        if b[i] == c[j]:
            sum += 1

print(sum)
