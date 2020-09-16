n = int(input())
p = input().split()
q = input().split()
p = [int(i) for i in p[1:]]
q = [int(i) for i in q[1:]]
k = set(p+q)
if len(k)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")