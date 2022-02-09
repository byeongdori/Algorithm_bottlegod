# 10816 - 숫자 카드 2
# 이분 탐색

import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
find = list(map(int, sys.stdin.readline().split()))

count = {}
for c in card:
    if c not in count:
        count[c] = 1
    else:
        count[c] += 1

for f in find:
    if f not in count:
        print(0, end=" ")
    else:
        print(count[f], end=" ")

