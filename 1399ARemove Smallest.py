n = int(input())

li = []
def solve(t,s):
    s.sort()
    # print(s)

    for j in range(1, t):
        if s[j] - s[j - 1] > 1:
            return "NO"

    return "YES"

for i in range(n):
    t = int(input())
    s = list(map(int, input().split()[:t]))
    li.append(solve(t,s))

for a in li:
    print(a)

# def solve(n, arr):
#
#     arr.sort()
#
#     for i in range(1, n):
#
#         if arr[i] - arr[i-1] > 1:
#             return "NO"
#
#     return "YES"
#
#
# if __name__ == "__main__":
#
#     t = int(input())
#
#     results = list()
#     for _ in range(0, t):
#         n = int(input())
#         arr = list(map(int, input().split(" ")))
#         results.append(solve(n, arr))
#     print(results)
#     for result in results:
#         print(result)