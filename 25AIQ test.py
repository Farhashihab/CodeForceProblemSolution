n = int(input())

s = list(map(int, input().split()))
ce=0
co =0
for i in range(len(s)):
    if s[i]%2==0:
        ce +=1
        leven = s.index(s[i])
    else:
        co+=1
        lodd = s.index(s[i])

if ce==1:
    print(leven+1)
else:
    print(lodd+1)
