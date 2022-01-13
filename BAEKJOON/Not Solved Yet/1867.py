# 1867 - 돌맹이 제거
# 이분 매칭, 최소 버텍스 커버

import sys

def check():
    for i in range(N):
        for j in range(N):
            if stone[i][j] != 0:
                return False
    return True

N, K = map(int, input().split())
stone = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    n, m = map(int, sys.stdin.readline().split())
    stone[n - 1][m - 1] = 1

visit_row = [0 for _ in range(N)]
visit_col = [0 for _ in range(N)]

answer = 0
# 행, 열 탐색
while 1:
    max_row = 0
    max_row_stone = 0

    max_col = 0
    max_col_stone = 0
    for i in range(N):
        row_stone, col_stone = 0, 0
        if visit_row[i] == 0:
            for j in range(N):
                if stone[i][j] == 1:
                    row_stone += 1

        if visit_col[i] == 0:
            for j in range(N):
                if stone[j][i] == 1:
                    col_stone += 1        

        if row_stone > max_row_stone:
            max_row_stone = row_stone
            max_row = i
        
        if col_stone > max_col_stone:
            max_col_stone = col_stone
            max_col = i

    # 돌맹이 제거
    if max_col_stone > max_row_stone:
        for i in range(N):
            if stone[i][max_col] > 0:
                stone[i][max_col] = 0
        visit_col[max_col] = 1
    else:
        for i in range(N):
            if stone[max_row][i] > 0:
                stone[max_row][i] = 0
        visit_row[max_row] = 1
    answer += 1

    # 다 제거했는지 체크
    if check():
        print(answer)
        break