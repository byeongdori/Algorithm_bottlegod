# 2178 - 미로 탐색

import sys
from collections import deque

N, M = map(int, input().split())

miro = []
for _ in range(N):
    miro.append(list(map(int,sys.stdin.readline().rstrip())))
visit = [[0 for _ in range(M)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# bfs
q = deque()
q.append([0, 0, 1])
visit[0][0] = 1
while q:
    current = q.popleft()
    current_x, current_y, dis = current[0], current[1], current[2]

    if current_x == N - 1 and current_y == M - 1:
        print(dis)
        break

    for i in range(4):
        nx = current_x + dx[i]
        ny = current_y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        else:
            if visit[nx][ny] == 0 and miro[nx][ny] == 1:
                q.append([nx, ny, dis + 1])
                visit[nx][ny] = 1