k = list(map(int, input().split()))
k.sort()

a = k[3] - k[2]
b = k[3] - k[1]
c = k[3] - k[0]
print(a, b, c)
