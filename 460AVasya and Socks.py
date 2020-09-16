n, m = map(int, input().split())
days = socks_left = n
while socks_left>=m:
    days +=int(socks_left/m)

    socks_left = int(socks_left/m) + socks_left%m


print(int(days))