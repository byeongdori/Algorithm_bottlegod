# 1753 - 최단경로
# 다익스트라 알고리즘

import sys, heapq

V, E = map(int, sys.stdin.readline().split())
K = int(input())

graph = [[] * (V + 1) for _ in range(V + 1)]
dis = [sys.maxsize] * (V + 1)
q = []

for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dis[K] = 0
heapq.heappush(q, (0, K))

while q:
    weight, node = heapq.heappop(q)
    for i, j in graph[node]:
        if weight + j < dis[i]:
            dis[i] = weight + j
            heapq.heappush(q, (dis[i], i))

for i in range(V):
    if dis[i + 1] == sys.maxsize:
        print("INF")
    else:
        print(dis[i + 1])