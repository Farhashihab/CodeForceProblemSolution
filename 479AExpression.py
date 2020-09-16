a = int(input())
b = int(input())
c = int(input())
s = []
s1 = a+(b*c)
s.append(s1)
s2 = a*b+c
s.append(s2)
s3 = a*(b+c)
s.append(s3)
s4 = a*b*c
s.append(s4)
s5 = a+b*c
s.append(s5)
s6 = (a+b)*c
s.append(s6)
s7 = a*b+c
s.append(s7)
s8 = a+b+c
s.append(s8)

print(max(s))