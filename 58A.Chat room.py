s = input()

a = 'hello'
x = 0
y = 0
for i in range(len(s)):
    if s[i] == a[x]:

        x += 1

        y += 1
        if y ==5:
            break
if y == 5:
    print("YES")
else:
    print("NO")
