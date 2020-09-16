a = int(input())
count = 0
j = []
for i in range(a):
    j.append(int(input()))

for i in range(len(j)):
    m = []
    n = j[i]
    if n % 10 != 0:
        k = (n % 10)
        m.append(k)
        count += 1
        n = n - k
    if n % 100 != 0:
        k = n % 100
        m.append(k)
        count += 1
        n = n - k
    if n % 1000 != 0:
        k = n % 1000
        m.append(k)
        count += 1
        n = n - k
    if n % 10000 != 0:
        k = n % 10000
        m.append(k)
        count += 1
        n = n - k
    if n % 10000 == 0 and n >= 10000:
        m.append(n)
        count += 1
    m.append(count)
    count = 0
    print(m[-1])
    print(*m[:-1])
