# 14499 - 주사위 굴리기

import sys

N, M, x, y, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
move = list(map(int,input().split()))

dice = [[0 for _ in range(4)] for _ in range(5)]
# 값 주사위에 복사 -> 주사위 굴리기

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
current_x, current_y = x, y

for i in move:
    # 현재 좌표 이동, 주사위 굴리기
    if current_x + dx[i - 1] >= N or current_x + dx[i - 1] < 0 or current_y + dy[i - 1] >= M or current_y + dy[i - 1] < 0:
        continue
    else:
        # 동쪽
        if i == 1:
            temp = dice[2][1]
            dice[2][1] = dice[4][2]
            dice[4][2] = dice[2][3]
            dice[2][3] = dice[2][2]
            dice[2][2] = temp
        # 서쪽
        elif i == 2:
            temp = dice[2][3]
            dice[2][3] = dice[4][2]
            dice[4][2] = dice[2][1]
            dice[2][1] = dice[2][2]
            dice[2][2] = temp
        # 북쪽
        elif i == 3:
            temp = dice[4][2]
            dice[4][2] = dice[1][2]
            dice[1][2] = dice[2][2]
            dice[2][2] = dice[3][2]
            dice[3][2] = temp
        # 남쪽
        elif i == 4:
            temp = dice[1][2]
            dice[1][2] = dice[4][2]
            dice[4][2] = dice[3][2]
            dice[3][2] = dice[2][2]
            dice[2][2] = temp
        current_x += dx[i - 1]
        current_y += dy[i - 1]

    # 밑면에 값 복사하기
    if arr[current_x][current_y] == 0:
        arr[current_x][current_y] = dice[4][2]
    else:
        dice[4][2] = arr[current_x][current_y]
        arr[current_x][current_y] = 0

    # 주사위 윗 면에 쓰인 수 출력
    print(dice[2][2])