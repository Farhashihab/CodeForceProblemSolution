import math


def findK(x, y, n):
    p = math.floor((n - y) / x)
    k = p * x + y
    return k


t = int(input())
for i in range(t):
    x, y, n = map(int, input().split())
    print(findK(x, y, n))
