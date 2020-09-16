n = int(input())
s = input().split()[:n]
s = [int(i) for i in s]
s.sort()
print(*s)
