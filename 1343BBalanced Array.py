n = int(input())
for i in range(n):
    a = int(input())
    if a %4==0:
        print("YES")
        fh = [int(i) for i in range(1, a + 1) if i % 2 == 0]
        sh = [int(i) for i in range(a) if i % 2 != 0]

        sh[-1]= sh[-1] + int(a / 2)
        print(*fh,*sh)
    else:
        print("NO")
