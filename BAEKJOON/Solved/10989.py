# 수 정렬하기 3
# 빠른 입출력 사용
# input의 범위가 0에서 10000사이이므로, 10001 크기의 배열 선언해 mapping

import sys

num_count = int(input())
arr = [0 for i in range(0, 10001)]

for i in range (0, num_count):
    temp = int(sys.stdin.readline())
    arr[temp] = arr[temp] + 1
for i in range(0, 10001):
    if arr[i] != 0:
        for j in range(0, arr[i]):
            sys.stdout.write(str(i) + "\n")
