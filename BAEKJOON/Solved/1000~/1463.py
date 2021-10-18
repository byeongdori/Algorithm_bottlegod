# 1463 - 1로 만들기
# DP
# f(x) = min(f(x-1) + 1 / f(x / 2) + 1 / f(x / 3) + 1)

import sys

n = int(input())
dp = [0 for _ in range (n + 1)]

# dp 값 채우기
for i in range (2, n + 1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[i // 3] + 1, dp[i // 2] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[i // 3] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
    else:
        dp[i] = dp[i - 1] + 1

print(dp[n])
