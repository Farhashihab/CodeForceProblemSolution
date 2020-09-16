t = int(input())


def calRec(a, b):
    area = min(max(2 * a, b), max(2 * b, a))
    return area * area


for i in range(t):
    a, b = map(int, input().split())
    print(calRec(a, b))
