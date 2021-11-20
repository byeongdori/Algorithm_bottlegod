# 1149 - RGB거리
# 동적 계획법

house = int(input())
coast = []
dp = [[0 for _ in range(3)] for _ in range(house)]

for i in range (house):
    coast.append(list(map(int, input().split())))

# i번째 집을 j색깔로 칠하고, i번째 까지 집을 칠하는 비용
# dp[i][j] = dp[i - 1][j - 1] + coast[j], dp[i - 1][j - 2] + coast[j]

dp[0][0], dp[0][1], dp[0][2] = coast[0][0], coast[0][1], coast[0][2]

for i in range(1, house):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + coast[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + coast[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + coast[i][2]

print(min(dp[house - 1][0], dp[house- 1][1], dp[house - 1][2]))