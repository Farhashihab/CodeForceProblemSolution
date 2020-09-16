n, t = map(int, input().split())
s = list(map(int, input().split()))
i = 1

while i < t:
    i += s[i - 1]
    print(i)

if i == t:
    print("YES")
else:
    print("NO")

# li = []
# for i in range(n - 1):
#     a = int(i) + s[i]+1
#     li.append(a)
#
# li = set(li)
# if t in li:
#     print("YES")
# else:
#     print("NO")
