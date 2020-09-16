t = int(input())


def honestCoach(arr):
    arr.sort()
    d = []
    for i in range(len(arr) - 1):
        d.append(arr[i + 1] - arr[i])
    return min(d)


for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    print(honestCoach(arr))
