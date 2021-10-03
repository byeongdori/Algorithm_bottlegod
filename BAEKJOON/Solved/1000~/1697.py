# 1697 - 숨바꼭질
# BFS

from collections import deque

N, K = map(int, input().split())
q = deque()
time = [0] * 100001

q.append(N)

while q:
    current = q.popleft()
    # print(current)
    if current == K:
        print(time[current])
        break
    for next in (current - 1, current + 1, current * 2):
        if 0 <= next <= 100000 and not time[next]:
            q.append(next)
            time[next] = time[current] + 1
