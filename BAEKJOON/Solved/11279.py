# 11279 - 최대 힙

import heapq, sys

max_heap = []

n = int(sys.stdin.readline())
for i in range (n):
    temp = int(sys.stdin.readline())
    if temp != 0:
        heapq.heappush(max_heap, (-temp, temp))
    else:
        if len(max_heap) != 0:
            print(heapq.heappop(max_heap)[1])
        else:
            print("0")
