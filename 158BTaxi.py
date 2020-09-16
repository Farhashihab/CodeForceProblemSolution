n = int(input())

s = input().split()
s.sort(reverse=False)
print(n)
print(s)
car = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0

for i in range(len(s)):
    if s[i] == "1":
        c1 += 1
    elif s[i] == "2":
        c2 += 1
    elif s[i] == "3":
        c3 += 1
    else:
        c4 += 1
print(c1, c2, c3, c4)

if c4 != 0:
    car = car + c4
    print(f"car for 4: {car}")
if c1 == c3:
    car = car + c1
    c1 = 0
    c3 = 0
else:
    if c3 > c1:
        car = car + c3
        print(f"car for c3>c1 {car}")
        c1 = 0
        print(f"c1 becomes :{c1}")
    else:
        if c3 != 0:
            car = car + c3
            c1 = c1 - c3
            print(f"remaning member of c1:{c1}")
            print(f"car for c3<c1 :{car}")
        else:
            if c1 % 4 == 0:

                car = car + int(c1 / 4)

            else:
                car = car + int(c1 / 4) + 1
            c1 = 0

if c2 > 2:
    if c2 % 2 == 0:
        car = car + int(c2 / 2)
        print(f"car for c2 if even: {car}")
        c2 = 0
    # else:
    #     car = car + int((c2 / 2))
    #     c2 = 2
    #     print(f"car for c2 if odd {car}")
c = c1 + c2
print(c)
if c != 0:
    if c < 4:
        car = car + 1
    elif c % 4 == 0:
        b = int(c/4)
        print(f"value of b {b}")
        car = car + b
        print(f"car for remaining c1 and c2 ==4 {car}")
    else:
        car = car + int(c / 4) + 1
        print(f"car for remaining c1 and c2  {car}")

print(int(car))
