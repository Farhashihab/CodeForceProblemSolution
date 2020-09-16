# a = [[0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0],
#      [0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0]]
a = []
for i in range(5):
    a.append([int(j) for j in input().strip().split(" ")])

for i in range(0,5):
    for j in range(0,5):
        if a[i][j] == 1:
            val = abs(i - 2) + abs(j - 2)
            print(val)
#
# print(matrix)
#
# for i in range(1, 5):
#     # print(i)
#     for j in range(1, 5):
#         if a[i][j] == '1':
#             print(i, j)
#             val = abs(i - 2) + abs(j - 2)
#             print(val)
