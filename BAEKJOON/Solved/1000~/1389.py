# 1389 - 케빈 베이컨의 6단계 법칙

from collections import deque

N, M = map(int, input().split())

friend = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
total_distance = 101
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    friend[a][b] = 1
    friend[b][a] = 1

for i in range(1, N + 1):
    q = deque()
    q.append(i)
    while q:
        current = q.popleft()
        for j in range(1, N + 1):
            if friend[current][j] == 1 and visit[j] == 0:
                visit[j] = visit[current] + 1
                q.append(j)
    if total_distance > sum(visit):
        total_distance = sum(visit)
        answer = i
    for j in range(1, N + 1):
        visit[j] = 0

print(answer)
        
                
