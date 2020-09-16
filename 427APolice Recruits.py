n = int(input())
s = list(map(int, input().split()))
p = 0
cnt = 0
for i in range(len(s)):
    if s[i] == -1:
        if p > 0:
            p -= 1
        else:
            cnt += 1
    else:
        p += s[i]
print(cnt)
