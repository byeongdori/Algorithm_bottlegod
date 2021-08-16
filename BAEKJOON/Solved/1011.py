# 1011 - Fly me to the Alpha Centauri
# 거리가 특정 수의 제곱일 때의 나열 순서 보며 법칙 찾기
import math

test_case = int(input())
for i in range(test_case):
    input_split = input().split()
    x = int(input_split[0])
    y = int(input_split[1])

    moving_count = 0
    distance = abs(x-y)
    current_distance = 0

    # 거리에 루트를 씌움
    n = int(math.sqrt(distance))
    moving_count += n
    l = (n*(n-1)/2)
    k = (n*(n+1)/2)

    remain_distance = distance - k
    
    if remain_distance == l:
        # l == remain
        moving_count += n-1
    elif remain_distance > l and remain_distance <= k:
        # l < remain <= k
        moving_count += n
    elif remain_distance > k:
        # remain > k
        moving_count += n+1

    print(moving_count)