# 2667 - 단지번호 붙이기

from collections import deque

N = int(input())

apart_map = []
for _ in range(N):
    apart_map.append(list(map(int, input())))

# dfs
visit = [[False for _ in range(N)] for _ in range (N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
answer = 0 
answer_size = []
for i in range(N):
    for j in range(N):
        if apart_map[i][j] > 0 and visit[i][j] == False:
            q.append([i, j])
            visit[i][j] = True
            answer += 1
            size = 1
            while q:
                temp = q.pop()
                cur_x, cur_y = temp[0], temp[1] 
                for k in range(4):
                    nx = cur_x + dx[k]
                    ny = cur_y + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if apart_map[nx][ny] > 0 and visit[nx][ny] == False:
                        q.append([nx, ny])
                        visit[nx][ny] = True
                        size += 1
            answer_size.append(size)

answer_size.sort()
print(answer)
for a in answer_size:
    print(a)
