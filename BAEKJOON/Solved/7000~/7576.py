# 7576 - 토마토
# DFS / BFS

import sys
from collections import deque

m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int,sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

check_tomato = False
answer = 0
q = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])

while q:
    size = len(q)
    for _ in range(size):
        temp = q.popleft()
        cur_x, cur_y = temp[0], temp[1]

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                q.append([nx, ny])

    answer += 1

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
print(answer - 1)