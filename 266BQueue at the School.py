n, t = map(int, input().split())

s = input().upper()
s = list(s)
for i in range(0, t):

    j = 0
    while j < n - 1:
        if s[j] == "B" and s[j + 1] == "G":
            s[j] = "G"
            s[j + 1] = "B"
            j += 2
        else:
            j += 1

print("".join(s))
