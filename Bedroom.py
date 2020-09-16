def solve(n, arr):

    max_elem = 100000 #highest value allowed for an element
    freq_map = [0] * (max_elem + 1)
    print(freq_map)

    for i in range(0, n):

        freq_map[arr[i]] += 1
        # print(freq_map)
    print(f"Frequency map array :{freq_map[arr[i]]}")

    dp = [0] * (max_elem + 1)
    print(dp)
    dp[0] = 0
    dp[1] = freq_map[1]
    print(f"Dp :{dp}")

    for num in range(2, max_elem + 1):
        print(dp[num],dp[num-1],dp[num-2],freq_map[num])
        dp[num] = max(dp[num-1], dp[num-2] + num * (freq_map[num]))
        # print(f"DUM :{dp[num]}")

    print(dp[max_elem])


if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().split(" ")))
    solve(n, arr)