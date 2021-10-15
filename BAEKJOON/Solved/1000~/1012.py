# 1012 - 유기농 배추

import sys
# 재귀 한도 10000으로 증가
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1,0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if arr[ny][nx] == 1:
                arr[ny][nx] = 0
                dfs(nx, ny)

case = int(input())

for _ in range(case):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    count = 0

    # graph 생성
    for _ in range(K):
        i, j = map(int, input().split())
        arr[j][i] = 1

    # 모든 graph에 대해 dfs 실행
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                dfs(j, i)
                count += 1
    print(count)
