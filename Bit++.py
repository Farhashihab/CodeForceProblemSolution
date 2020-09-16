n = int(input())

x = 0
for i in range(n):
    operator = input()
    if operator[1] == '+':
        x += 1
    else:
        x -= 1

print(x)
