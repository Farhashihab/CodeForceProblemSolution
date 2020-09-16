n, m = map(int, input().split())

s = input().split()[:m]
s = [int(s[i]) for i in range(m)]
s.sort()
d = []
j = n
for i in range(m):
    k = s[i:n]

    if len(k) >= j:
        k.sort()
        diff = int(k[-1]) - int(k[0])

        d.append(diff)
    n += 1

print(min(d))
