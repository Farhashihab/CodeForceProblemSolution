a, b = map(int, input().split())

for i in range(b):
    a = str(a)

    if a[-1] == "0":
        a = int(int(a) / 10)

    else:
        a = int(a) - 1

print(a)
