n = int(input())
s = input().split()
r = []
for i in range(1, n + 1):
    r.append(int(s.index(str(i))) + 1)

b =' '.join([str(elem) for elem in r])
print(b)
