a, b = map(int, input().split())

if a <= b:
    j = int((b - a) / 2)
    print(a, j)
else:
    j = int((a - b) / 2)
    print(b, j)
