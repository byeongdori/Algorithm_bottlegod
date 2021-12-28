# 1311 - 할 일 정하기 1
# dp, 비트 마스킹
import sys

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))
dp = [sys.maxsize] * (1 << N)
dp[0] = 0

# dp 진행
for i in range(1 << N):
    k = 0
    for j in range(N):
        if i & (1 << j):
            k += 1
    for j in range(N):
        if i & (1 << j) == 0 and dp[i|(1 << j)] > dp[i]+cost[k][j]:
            dp[i|(1 << j)] = dp[i] + cost[k][j]

print(dp[-1])
