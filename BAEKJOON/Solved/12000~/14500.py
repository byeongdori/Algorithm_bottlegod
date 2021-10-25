# 14500 - 테트로미노

import sys

tetris = [([0, 0], [0, 1], [0, 2], [0, 3]),  # 일자 모양
         ([0, 0], [1, 0], [2, 0], [3, 0]),
         ([0, 0], [0, 1], [1, 1], [1, 0]),  # 정사각형 모양
         # ㄴ 모양
         ([0, 0], [1, 0], [1, 1], [1, 2]),
         ([0, 0], [0, 1], [1, 0], [2, 0]),
         ([0, 0], [0, 1], [0, 2], [1, 2]),
         ([0, 1], [1, 1], [2, 1], [2, 0]),
         ([0, 0], [0, 1], [1, 1], [2, 1]),
         ([1, 0], [1, 1], [1, 2], [0, 2]),
         ([0, 0], [1, 0], [2, 0], [2, 1]),
         ([0, 0], [1, 0], [0, 1], [0, 2]),
         # ㄴ, ㄱ 합친 모양
         ([0, 0], [1, 0], [1, 1], [2, 1]),
         ([1, 0], [1, 1], [0, 1], [0, 2]),
         ([2, 0], [1, 0], [1, 1], [0, 1]),
         ([0, 0], [0, 1], [1, 1], [1, 2]),
         # ㅜ 모양
         ([0, 0], [0, 1], [1, 1], [0, 2]),
         ([1, 0], [0, 1], [1, 1], [2, 1]),
         ([1, 0], [1, 1], [1, 2], [0, 1]),
         ([0, 0], [1, 0], [1, 1], [2, 0])]
 
def tetri_sum(r, c, arr):  # t: 해당 tetromino 의 좌표 모음
    sum = 0
    global N, M
    for dx, dy in arr:
        nx = r + dx
        ny = c + dy
        if 0 <= nx < N and 0 <= ny < M:
            sum += board[nx][ny]
        else:
            return -1
    return sum
 
 
N, M = map(int, sys.stdin.readline().split())
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for r in range(N):
    for c in range(M):
        for tetromino in tetris:
            answer = max(answer, tetri_sum(r, c, tetromino))

print(answer)