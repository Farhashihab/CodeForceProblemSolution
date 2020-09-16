s1 = input()
s2 = input()
k = input()
s = s1+s2
s = sorted(s,reverse=False)
k = sorted(k,reverse=False)


if s == k:
    print("YES")
else:
    print("NO")