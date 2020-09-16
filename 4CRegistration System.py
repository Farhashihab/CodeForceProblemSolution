n = int(input())
# emlist = []
# f = 0
d = {}

for i in range(n):
    k = input()
    if k in d:
        print(k+str(d[k]))
        d[k]+=1
    else:
        print("OK")
        d[k]=1


# for i in range(n):
#     k = input()
#     if k not in emlist:
#         print('OK')
#         emlist.append(k)
#     else:
#         f = emlist.count(k)
#         emlist.append(k)
#         print(f"{k}{f}")
