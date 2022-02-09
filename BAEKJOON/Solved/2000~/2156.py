# 2156 - 포도주 시식
# 다이나믹 프로그래밍

# i번째 까지 최대로 많이 먹는 경우
# i번째를 먹느냐, 안먹느냐로 구분
# dp[i] = max(current[i] + max(current[i - 1] + dp[i - 3], dp[i - 2]), dp[i - 1])

n = int(input())
podo = []
podo.append(0)
for _ in range(n):
    podo.append(int(input()))

dp = [0] * (n + 1)
dp[1] = podo[1]

if n >= 2:
    dp[2] = podo[1] + podo[2]

if n >= 3:
    for i in range(3, n + 1):
        dp[i] = max(podo[i] + max(podo[i - 1] + dp[i - 3], dp[i - 2]), dp[i - 1])

print(dp[n])