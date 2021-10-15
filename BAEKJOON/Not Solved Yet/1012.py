# 1012 - 유기농 배추

case = int(input())

M, N, K = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]
count = 0
for _ in range(K):
    i, j = map(int, input().split())
    arr[i][j] = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visit[i][j] == False:
            # bfs
            pass

