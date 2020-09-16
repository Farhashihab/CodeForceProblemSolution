n, k = map(int, input().split())
s = list(map(int, input().split()))
counter = 0
for i in range(len(s)):

    if abs(s[i] - 5) >= k:
        counter += 1

if counter >= 3:
    print(int(counter / 3))
else:
    print("0")
