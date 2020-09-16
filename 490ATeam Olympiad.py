n = int(input())
sl = list(map(int, input().split()))
p = []
m = []
pe = []

for i in range(len(sl)):
    if sl[i] == 1:
        p.append(i + 1)
    elif sl[i] == 2:
        m.append(i + 1)
    else:
        pe.append(i + 1)
p.sort(reverse=True)
m.sort(reverse=True)
pe.sort(reverse=True)
# print(p,m,pe)
team = min(len(p), len(m), len(pe))
# print(team)
if team>0:
    print(team)
    for i in range(team):
        print(p[i],m[i],pe[i])
else:
    print(team)

