n = int(input())

for i in range(n):
    l = []
    k = input()
    for i in range(0, len(k), 2):
        b = k[i:i + 2]
        if i == 0:
            l.append(b)
        else:
            l.append(b[-1])
    print("".join(l))

