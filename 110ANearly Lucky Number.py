n = input()

s = 0

for i in range(len(n)):
    if n[i] == "4" or n[i] == "7":
        s += 1

if s == 4 or s == 7:
    print("YES")
else:
    print("NO")
