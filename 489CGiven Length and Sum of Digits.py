m, s = map(int, input().split())
maxi = ""
mini = ""

if s == 0:
    if m == 1:
        print("0 0")
    else:
        print("-1 -1")
else:
    for i in range(m):
        k = min(9, s)
        maxi += str(k)
        s -= k
    if s > 0:
        print("-1 -1")
        # break
    else:
        mini = maxi[::-1]

        while mini[0] == "0":
            mini = list(maxi[::-1])

            mini = mini[1:]
            for i in range(len(mini)):

                if int(mini[i]) > 0:
                    u = int(mini[i]) - 1

                    mini[i] = u
                    break

            d = str(1) + ''.join(map(str, mini))
            mini = d
        print(mini, end=" ")
        print(maxi)
