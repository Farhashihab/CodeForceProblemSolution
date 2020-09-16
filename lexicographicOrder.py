s1 = input().lower()
s2 = input().lower()
if s1 == s2:
    print('0')

for i in range(len(s1)):
    if s1[i] < s2[i]:
        print('-1')
        break
    if s1[i] > s2[i]:
        print('1')
        break

print(valueS1)
print(valueS2)

# for i in range(len(s1)):
#     if s1[i] == s2[i]:
#         x = 0
#     else:
#         if ord(s1[i]) > ord(s2[i]):
#             x = 1
#         else:
#             x = -1
# print(x)
