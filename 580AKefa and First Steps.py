n = int(input())
l = list(map(int, input().split()))
p = 1
i = 0
m = 1
while i < n - 1:
    if l[i] <= l[i + 1]:
        p += 1
        if p > m:
            m = p
    else:
        p = 1
    i += 1
print(m)
