n = int(input())

for i in range(n):
    a = int(input())
    for j in range(2, a):
     
        b = a / (pow(2, j) - 1)

        if b.is_integer():
            print(int(b))
            break
