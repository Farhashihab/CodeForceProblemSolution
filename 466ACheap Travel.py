n, m, a, b = map(int, input().split())
total = 0
if m * a <= b:
    z = n * a
else:

    z = (int(n / m) * b) + min((n % m) * a, b)
print(int(z))
