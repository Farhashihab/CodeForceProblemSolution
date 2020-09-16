n = int(input())
s = list(map(int, input().split()))
s.sort()
count = 0
for i in range(n):
    count += (s[-1] - s[i])
print(count)
