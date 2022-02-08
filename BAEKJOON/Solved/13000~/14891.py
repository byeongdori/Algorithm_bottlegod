# 14891 - 톱니바퀴

import sys
from collections import deque

q = {}

def check_right(start, dir):
    
    if start >= 3 or q[start][2] == q[start + 1][6]:
        return

    if q[start][2] != q[start + 1][6]:
        check_right(start + 1, -dir)
        q[start + 1].rotate(dir)


def check_left(start, dir):
    
    if start < 1 or q[start][6] == q[start - 1][2]:
        return

    if q[start][6] != q[start - 1][2]:
        check_left(start - 1, -dir)
        q[start - 1].rotate(dir)


for i in range(4):
    q[i] = deque(list(map(int, input())))

K = int(input())
for _ in range(K):
    n, dir = map(int, input().split())
    check_right(n - 1, -dir)
    check_left(n - 1, -dir)
    q[n - 1].rotate(dir)
    # print(q)

# print(q)

answer = 0
for i in range(4):
    if q[i][0] == 1:
        answer += pow(2, i)

print(answer)
