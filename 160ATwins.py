n = int(input())
noCoins = input().split()

noCoins = [int(noCoins[i]) for i in range(len(noCoins))]
noCoins.sort(reverse=True)

print(noCoins)

s = 0
# i = 0
if len(noCoins) == 1:
    print("1")
else:
    for i in range(len(noCoins)):
        print(i)
        print(f"value of i {noCoins[i]}")
        s += noCoins[i]
        print(f"sum : {s}")
        i += 1
        print(f"rest value {noCoins[i]}")
        print(noCoins[i:])
        print(f"baki sum {sum(noCoins[i:])}")
        rstsum = sum(noCoins[i:])
        if s > rstsum:
            print(i)
            break
