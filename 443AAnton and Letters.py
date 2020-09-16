import re

s = input().split()
s = " ".join(s)
res1 = " ".join(re.split('[^a-zA-Z]*', s))
print(len(set(res1))-1)
