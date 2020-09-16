n = int(input())
j = []


def cont(a, b):
    if a % b == 0:
        j.append(0)
    elif b > a:
        j.append(b - a)
    else:
        h = a % b
        ans = b - h
        j.append(ans)

for i in range(n):
    a, b = map(int, input().split())
    cont(a,b)

print(*j, sep="\n")
