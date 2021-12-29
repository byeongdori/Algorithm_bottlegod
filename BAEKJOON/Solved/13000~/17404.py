# 17404 - RGB거리 2
# 조건이 추가된 다이나믹 프로그래밍
import sys

N = int(input())

dp = [[0 for _ in range(3)] for _ in range(N)]
cost = []
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

answer = 1000 * 1000 + 1
for k in range(3):
    # 첫번째 집 색깔 고정
    for i in range(3):
        if i == k:
            dp[0][i] = cost[0][i]
        else:
            dp[0][i] = 1001

    for i in range(1, N):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

    for i in range(3):
        if i == k:
            continue
        else:
            answer = min(answer, dp[N-1][i])

print(answer)