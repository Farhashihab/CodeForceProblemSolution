n = int(input())

s = input().split()
sum = 0

for i in range(len(s)):
    sum = sum+int(s[i])
print(sum/n)