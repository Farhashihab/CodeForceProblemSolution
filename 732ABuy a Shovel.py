n, k = map(int, input().split())
count = 0
b = True
h = 1
while b:
    count += 1
    h = n * count
    if (h % 10 == 0) or h % 10 == k:
        b = False
print(count)

# for i in range(1, n):
#     count += n
#     if count % 10 == 0 or count % 10 == k:
#         print(i)
#         break
#     else:
#         continue

# for i in range(n):
#     if n >= k:
#
#         a = int(n % 10)
#         print(f"fffff:{a}")
#         if a == k or a == 0:
#             break
#         else:
#             n = n + p
#             count += 1
#     else:
#         f = True
#         while f:
#             if k % n == 0:
#                 count = int(k / n)
#                 f = False
#
#             elif n % 10 == 0:
#                 count = count
#                 f = False
#             else:
#                 n = n + p
#                 count += 1
#
#
#
# print(count)
