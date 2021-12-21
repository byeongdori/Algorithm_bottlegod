# 14502 - 연구소
# BFS, 브루트 포스

from collections import deque

answer = -1

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
def virusbfs(area):

    q = deque()
    for i in range(N):
        for j in range(M):
            if area[i][j] == 2:
                q.append([i, j])

    while q:
        current = q.popleft()
        for i in range(4):
            ny = current[0] + dy[i]
            nx = current[1] + dx[i]
            if nx >= 0 and nx < M and ny >= 0 and ny < N:
                if area[ny][nx] == 0:
                    area[ny][nx] = 2
                    q.append([ny, nx])
    
    safe_area = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == 0:
                safe_area = safe_area + 1
    
    print(safe_area)
    return safe_area

def wallcreate(wall_count):
    global answer
    if wall_count == 3:
        print("hello")
        temp = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                temp[i][j] = area[i][j]
        answer = max(answer, virusbfs(temp))
        return

    for i in range(N):
        for j in range(M):
            if area[i][j] == 0:
                area[i][j] = 1
                wallcreate(wall_count + 1)
                area[i][j] = 0

N, M = map(int, input().split())

area = []
for i in range(N):
    area.append(list(map(int, input().split())))

wallcreate(0)
print(answer)