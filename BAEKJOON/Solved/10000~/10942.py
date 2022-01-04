# 10942 - 팰린드롬?
# palindrom[S][E] => palindrom[S + 1][E - 1] == 1 and arr[S] == arr[E]

import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
M = int(input())

palindrom = [[0 for _ in range(N)] for _ in range(N)]

# 길이 1인 경우
for i in range(N):
    palindrom[i][i] = 1

# 길이 2인 경우
for i in range(N - 1):
    if arr[i] == arr[i + 1]:
        palindrom[i][i + 1] = 1

# 길이 3이상인 경우
for i in range(2, N):
    for j in range(N - i):
        # j ~ j + 1
        if palindrom[j + 1][j + i - 1] == 1 and arr[j] == arr[j + i]:
            palindrom[j][j + i] = 1

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(palindrom[S - 1][E - 1])

