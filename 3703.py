n, m = map(int, input().split())

dp = []
for i in range(n):
    dp.append([])
    dp[i] = list(map(int, input().split()))


for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            pass
        elif i == 0 and j != 0:
            dp[i][j] += dp[i][j-1]
        elif j == 0 and i != 0:
            dp[i][j] += dp[i-1][j]
        else:
            dp[i][j] += max(dp[i][j-1], dp[i-1][j])

print(dp[n-1][m-1])


