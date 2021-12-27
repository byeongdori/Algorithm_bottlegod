# 1311 - 할 일 정하기 1
# dp, 비트 마스킹

import sys

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))
dp = [sys.maxsize] * (1 << N)

# dp 진행

print(dp)