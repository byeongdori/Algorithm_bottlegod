# 1806 - 부분합
# 투 포인터

import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))
min_len = sys.maxsize

sum_arr = [0]
for i in range (1, len(arr) + 1):
    sum_arr.append(sum_arr[i - 1] + arr[i - 1])

start, end = 0, 1
while start < N:
    temp = sum_arr[end] - sum_arr[start]
    if temp >= S:
        min_len = min(min_len, end - start)
        start += 1
    else:
        if end < N:
            end += 1
        else:
            start += 1

if min_len == sys.maxsize:
    print(0)
else:
    print(min_len)
