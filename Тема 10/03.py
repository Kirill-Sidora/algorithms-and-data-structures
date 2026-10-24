def count_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for k in range(1, n + 1):
        for i in range(k, n + 1):
            dp[i] += dp[i - k]

    return dp[n]

def count_partitions_limited(n, max_part):
    dp = [0] * (n + 1)
    dp[0] = 1

    for k in range(1, max_part + 1):
        for i in range(k, n + 1):
            dp[i] += dp[i - k]
            
    return dp[n]