n, m = map(int, input().split())
s = list(map(int, input().split()))

sum = 0
i = 1
f = 1
for i in range(1, m + 1):
    j = f
    if s[i - 1] >= j:
        k = (s[i - 1] - j)
        f = s[i - 1]
        sum += k
    else:
        k = n - j + s[i - 1]

        f = s[i - 1]
        sum += k

print(sum)
