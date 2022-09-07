a, b = map(int, input().split())

dp = {b:0}

def fn(i, b):
    # print(i, b)
    if i in dp:
        return dp[i]
    else:
        if abs(i-b) >= 8:
            if i < b:
                dp[i] = fn(i+10, b) + 1
            else:
                dp[i] = fn(i-10, b) + 1
        elif 3 <= abs(i-b) < 8:
            if i < b:
                dp[i] = fn(i+5, b) + 1
            else:
                dp[i] = fn(i-5, b) + 1
        elif 1 <= abs(i-b) < 3:
            if i < b:
                dp[i] = fn(i+1, b) + 1
            else:
                dp[i] = fn(i-1, b) + 1
        return dp[i]


print(fn(a, b))




