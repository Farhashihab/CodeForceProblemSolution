n = int(input())
sum = 0

if n >= 100:
    k = int(n / 100)
    sum += k
    n = n % 100
    print(f"new n {n}")
    print(f"sum: {sum}")
    if n >= 20:
        k = int(n / 20)
        sum += k
        n = n % 20
        print(f"new n {n}")
        print(f"sum: {sum}")
        if n >= 5:
            k = int(n / 5)
            sum += k
            n = n % 5
            print(f"new n {n}")
            print(f"sum: {sum}")
            if n >= 1:
                k = int(n / 1)
                sum += k
                n = n % 1
                print(f"new n {n}")
                print(f"sum: {sum}")
elif n >= 20:
    k = int(n / 20)
    sum += k
    n = n % 20
    print(f"new n {n}")
    print(f"sum: {sum}")
    if n >= 5:
        k = int(n / 5)
        sum += k
        n = n % 5
        print(f"new n {n}")
        print(f"sum: {sum}")
        if n >= 1:
            k = int(n / 1)
            print(k)
            sum += k
            n = n % 1
            print(f"new n {n}")
            print(f"sum: {sum}")
    elif n>=1:
        k = int(n / 1)
        print(k)
        sum += k
        n = n % 1
        print(f"new n {n}")
        print(f"sum: {sum}")
elif n>=5:
    k = int(n / 5)
    sum += k
    n = n % 5
    print(f"new n {n}")
    print(f"sum: {sum}")
    if n >= 1:
        k = int(n / 1)
        print(k)
        sum += k
        n = n % 1
        print(n)
        print(f"sum: {sum}")
elif n>=1:
    k = int(n / 1)
    print(k)
    sum += k
    n = n % 1
    print(f"new n {n}")
    print(f"sum: {sum}")



# elif n >= 20:
#     k = int(n / 20)
#     sum += k
#     n = n - (20 * k)
#     print(n)
#
# print(int(225 / 100))
