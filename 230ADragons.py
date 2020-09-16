s, n = map(int, input().split())
ys = 1
ne = 0
xlis = []

for i in range(n):
    x = list(map(int, input().split()))
    xlis.append(x)
xlis.sort()

for i in range(n):
    if s > xlis[i][0]:
        b = xlis[i][1]
        s = s + b

        # ys += 1

    else:
        # ne += 1
        ys = 0
        break

if ys:
    print("YES")
else:
    print("NO")