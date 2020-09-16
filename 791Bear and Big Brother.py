a, b = map(int, input().split())

c = True
i = 0
while c:
    a *= 3
    b *= 2
    i += 1
    if a > b:
        c = False
        print(i)
