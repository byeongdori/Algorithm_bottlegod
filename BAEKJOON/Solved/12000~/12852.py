# 12852 - 1로 만들기 2
# DP, 역추적
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

# 역추적
while n >= 1:
    sys.stdout.write(str(n))
    if n != 1:
        sys.stdout.write(" ")
    if n % 3 == 0 and n % 2 == 0:
        temp = min(dp[n - 1] + 1, dp[n // 3] + 1, dp[n // 2] + 1)
        if temp == dp[n - 1] + 1:
            n = n - 1
        elif temp == dp[n // 3] + 1:
            n = n // 3
        else:
            n = n // 2
    elif n % 3 == 0:
        if dp[n - 1] >= dp[n // 3]:
            n = n // 3
        else:
            n = n - 1
    elif n % 2 == 0:
        if dp[n - 1] >= dp[n // 2]:
            n = n // 2
        else:
            n = n - 1
    else:
        n = n - 1