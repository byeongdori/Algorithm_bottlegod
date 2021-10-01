# 7562 - 나이트의 이동
# Bfs 사용

from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

case = int(input())

for _ in range(case):
    size = int(input())
    current = list(map(int,input().split()))
    dest = list(map(int,input().split()))
    
    graph = [[0 for _ in range(size)] for _ in range(size)]
    q = deque()
    q.append([current[0], current[1]])
    while q:
        x, y = q.popleft()
        if x==dest[0] and y==dest[1]:
            break
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x >= size or next_y < 0 or next_y >= size:
                continue
            if graph[next_x][next_y] == 0:
                graph[next_x][next_y] = graph[x][y] + 1
                q.append([next_x, next_y])
    print(graph[dest[0]][dest[1]])
