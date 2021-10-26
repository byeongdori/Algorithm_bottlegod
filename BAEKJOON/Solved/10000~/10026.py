# 10026 - 적록색약

from collections import deque

def bfs(i, j):
    q = deque()
    q.append([i, j])
    while q:
        current = q.popleft()
        color = picture[current[0]][current[1]]
        for i in range(4):
            nx = current[0] + next[i][0]
            ny = current[1] + next[i][1]
            if nx >= 0 and nx < N and ny >=0 and ny < N:
                if visit_1[nx][ny] == 0 and picture[nx][ny] == color:
                    q.append([nx, ny])
                    visit_1[nx][ny] = 1

def bfs_blind(i, j):
    q = deque()
    q.append([i, j])
    while q:
        current = q.popleft()
        color = picture[current[0]][current[1]]
        for i in range(4):
            nx = current[0] + next[i][0]
            ny = current[1] + next[i][1]
            if nx >= 0 and nx < N and ny >=0 and ny < N:
                if visit_2[nx][ny] == 0:
                    if (picture[nx][ny] == 'R' or picture[nx][ny] == 'G') and (color == 'R' or color == 'G'):
                        q.append([nx, ny])
                        visit_2[nx][ny] = 1
                    elif color == picture[nx][ny]:
                        q.append([nx, ny])
                        visit_2[nx][ny] = 1

next = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N = int(input())
picture = []

for i in range(N):
    picture.append(list(map(str, input())))

visit_1 = [[0 for _ in range(N)] for _ in range(N)]
visit_2 = [[0 for _ in range(N)] for _ in range(N)]

area_1, area_2 = 0, 0

for i in range(N):
    for j in range(N):
        if visit_1[i][j] == 0:
            bfs(i, j)
            area_1 += 1

for i in range(N):
    for j in range(N):
        if visit_2[i][j] == 0:
            bfs_blind(i, j)
            area_2 += 1

print(area_1, area_2)
