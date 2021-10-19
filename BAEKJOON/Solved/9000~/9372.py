# 9372 - 상근이의 여행

from collections import deque
import sys

def bfs(i):
    count = 0 
    q = deque()
    q.append(i)

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visit[nx] == 0:
                visit[nx] = 1
                q.append(nx)
                count += 1
    
    return count


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visit = [0 for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    total_count = 0
    for i in range(N):
        if visit[i] == 0:  # 아직 방문한 도시가 아니라면
            total_count += bfs(i)

    print(total_count - 1)
