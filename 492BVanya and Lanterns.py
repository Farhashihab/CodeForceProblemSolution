n, l = map(int, input().split())
k = list(map(int, input().split()))
k.sort()
m = 0
for i in range(0,len(k) - 1):
    if k[i + 1] - k[i] > m:
        m = k[i + 1] - k[i]
x = k[0]
y = m / 2
j = max(x, y)
z = l - k[n - 1]
ans = max(j, z)
print("%.10f" % ans)
