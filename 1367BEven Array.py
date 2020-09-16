t = int(input())


def evenarray(arr):
    c = 0
    ce = 0
    co = 0
    el = []
    ol = []
    for i in range(len(arr)):
        if i % 2 == 0:
            el.append(arr[i])
        else:
            ol.append(arr[i])
    for i in range(len(el)):
        if el[i] % 2 != 0:
            ce += 1
    for i in range(len(ol)):
        if ol[i] % 2 != 1:
            co += 1
    if ce == 0 and co == 0:
        print("0")
    elif ce == co:
        print(ce)
    else:
        print("-1")


for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    evenarray(arr)
