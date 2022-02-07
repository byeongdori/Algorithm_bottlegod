# 14891 - 톱니바퀴

import sys
from collections import deque

# queue 쓰는 걸로 다시..
q = {}

for i in range(4):
    q[i] = deque(list(map(int, input())))

q[1].rotate(1)
print(q[1])