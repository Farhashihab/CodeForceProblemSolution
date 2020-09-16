import math

n, h = map(int, input().split())

s = input().split()
count = 0

for i in range(len(s)):
    count += math.ceil(int(s[i]) / h)

print(count)
