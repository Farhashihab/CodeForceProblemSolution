n, k = map(int, input().split())
reT = 240 - k
s = 0
m = 0

for i in range(1, n + 1):
    s += (5 * i)
    if s <= reT:
        m += 1

print(m)
