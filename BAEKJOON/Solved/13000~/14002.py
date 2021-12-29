# 14002 - 가장 긴 증가하는 부분 수열 4
# DP

import sys

size = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(len(arr))]
dp_index = [-1 for _ in range(len(arr))]
result_arr = []

dp[0] = 1
max_index = 0 
for i in range(1, len(arr)):
    temp = 0
    for j in range(0, i):
        if arr[i] > arr[j] and dp[j] > temp:
            temp = dp[j]
            dp_index[i] = j

    dp[i] = temp + 1
    if dp[i] > dp[max_index]:
        max_index = i

print(max(dp))
i = max_index
while i != -1:
    result_arr.append(arr[i])
    i = dp_index[i]

result_arr.reverse()
print(*result_arr)
