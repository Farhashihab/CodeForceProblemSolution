def giftsFixing(arr1, arr2):
    c = 0
    for i in range(len(arr1)):
        minarr1 = min(arr1)
        minarr2 = min(arr2)
        c += max((arr1[i] - minarr1), (arr2[i] - minarr2))
    return c


t = int(input())
for i in range(t):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    print(giftsFixing(arr1,arr2))
