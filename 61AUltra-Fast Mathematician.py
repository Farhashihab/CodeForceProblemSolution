s = input()
s2 = input()
k = []
for i in range(len(s)):
    if (s[i]=='1' and s2[i]=='1') or (s[i]=='0' and s2[i]=='0'):
        k.append("0")
    else:
        k.append("1")

print("".join(k))
