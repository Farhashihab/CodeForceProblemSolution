n = int(input())
a = ["I hate", "I love"]
s = " "
for i in range(n):
    if i % 2 != 0:
        s = s + a[1] + " " + "that" + " "
    else:
        s = s + a[0] + " " + "that" + " "

k = s.split()
j = ['it']
k = k[:-1]+j
print(" ".join(k))
