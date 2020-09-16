s = list(map(int,input().split()))
s.sort()

count = 0
count+=(s[1]-s[0])
count+=(s[2]-s[1])

print(count)