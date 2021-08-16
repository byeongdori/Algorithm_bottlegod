# 1002 - 터렛

import math
test_case = int(input())

for i in range (0, test_case):
    input_split = input().split()
    x1 = int(input_split[0])
    y1 = int(input_split[1])
    r1 = int(input_split[2])
    x2 = int(input_split[3])
    y2 = int(input_split[4])
    r2 = int(input_split[5])

    # 두 원의 중심 사이의 거리
    distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))

    # 안 만나는 경우
    if distance > r1 + r2 or distance < abs(r1 - r2):
        print(0)
    # 한 점에서 만나는 경우
    elif distance == r1 + r2 or (distance == abs(r1 - r2) and distance != 0):
        print(1)
    # 두 점에서 만나는 경우
    elif distance < r1 + r2 and distance > abs(r1 - r2):
        print(2)
    # 두 원이 같은 경우
    elif distance == 0 and r1 == r2:
        print(-1)