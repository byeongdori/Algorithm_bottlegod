# 2751 - 수 정렬하기 2
# 빠른 입출력 사용

import sys

num_count = int(input())
arr = []
for i in range (0, num_count):
    arr.append(int(sys.stdin.readline()))
for i in sorted(arr):
    sys.stdout.write(str(i) + "\n")
