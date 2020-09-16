x = int(input())
def solve(n):

    count = 0
    while n > 0:

        count += (n & 1)
        print(f"count: {count}")
        n >>= 1
        print(f"value of n:{n}")

    print(count)
solve(x)
