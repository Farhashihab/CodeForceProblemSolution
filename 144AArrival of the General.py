n = int(input())

s = input().split()
s = [int(x) for x in s]

ma = 0
mi = n - 1
for i in range(n):
    if s[i] > s[ma]:
        ma = i
    if s[i] <= s[mi]:
        mi = i

if mi > ma:
    print(n + ma - mi - 1)
else:
    print(n + ma - mi - 2)
