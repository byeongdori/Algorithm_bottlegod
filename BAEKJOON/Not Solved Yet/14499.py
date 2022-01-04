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
    if current_x + dx[i] > N or current_x + dx[i] < 0 or current_y + dy[i] > M or current_y + dy[i] < 0:
        continue
    else:
        # 동쪽
        if i == 1:
            pass
        # 서쪽
        elif i == 2:
            pass
        # 북쪽
        elif i == 3:
            pass
        # 남쪽
        elif i == 4:
            pass
        current_x += dx[i]
        current_y += dy[i]
    # 밑면에 값 복사하기
    if arr[current_x][current_y] == 0:
        arr[current_x][current_y] = dice[2][4]
        dice[2][4] = 0
    else:
        dice[2][4] = arr[current_x][current_y]
        arr[current_x][current_y] = 0

    # 주사위 윗 면에 쓰인 수 출력
    print(dice[2][2])