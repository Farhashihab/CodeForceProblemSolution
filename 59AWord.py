s = input()
u = 0
l = 0
for i in range(len(s)):
    if s[i].isupper():
        u += 1
    else:
        l += 1

if l >= u:
    print(s.lower())
else:
    print(s.upper())
