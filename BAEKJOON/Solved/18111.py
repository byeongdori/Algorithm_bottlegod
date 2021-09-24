# 18111 - 마인크래프트
# pypy3 사용해서 통과

import sys

n, m, b = map(int, sys.stdin.readline().split())

land = []
land_sum = 0

for i in range(n):
    land.append(list(map(int, sys.stdin.readline().split())))
    land_sum += sum(land[i])

min_land = min(map(min,land))
max_land = max(map(max,land))
height, ans = 0, 10000000000000000

for h in range(min_land, max_land + 1):
    remove, add = 0, 0
    if (land_sum + b) < (n * m * h):
        break
    for i in range(n):
        for j in range(m):
            if land[i][j] > h:
                remove += land[i][j] - h
            else:
                add += h - land[i][j]
    if b + remove - add >= 0 and 2 * remove + add <= ans:
        ans = 2 * remove + add
        height = h

print(ans, height)

            