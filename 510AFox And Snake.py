n, m = map(int, input().split())
x = '#'
y = '.'

for i in range(1, n + 1):
    if i % 2 != 0:
        for j in range(m):
            print(f"{x}", end='')
        print()
    else:
        if i % 4 == 0:
            print(x, end='')
            for j in range(m - 1):
                print(f"{y}", end='')
        else:
            for j in range(m - 1):
                print(f"{y}", end='')
            print(x, end='')

        print()
