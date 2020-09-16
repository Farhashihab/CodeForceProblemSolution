t = int(input())


def kl(a, b, k, n):
    s = 0
    for i in range(k):
        s += max(a[i], b[i])
    for i in range(k, n):
        s += a[i]
    return s


for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)

    print(kl(a, b, k, n))
