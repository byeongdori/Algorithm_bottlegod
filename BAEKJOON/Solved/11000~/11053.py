# 11053 - 가장 많이 증가하는 부분 수열

N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = 1

for i in range(1, len(dp)):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))