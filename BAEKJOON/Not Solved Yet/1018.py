# 1018 - 체스판 다시 칠하기
# 왜 안됌? - 아 퍼컬 라컬 둘다 같은 경우;;;

def check_board(arr, i, j):
    first_color = arr[i][j]
    last_color = arr[i + 7][j + 7]
    temp = (i + j) % 2
    count_first, count_last =0, 0
    for a in range(8):
        for b in range(8):
            check = (a + i + b + j) % 2
            if check == temp and first_color == arr[a + i][b + j]:
                continue
            elif check != temp and first_color != arr[a + i][b + j]:
                continue
            else:
                count_first += 1
    
    for a in range(8):
        for b in range(8):
            check = (a + i + b + j) % 2
            if check == temp and last_color == arr[a + i][b + j]:
                continue
            elif check != temp and last_color != arr[a + i][b + j]:
                continue
            else:
                count_last += 1
    
    return min(count_first, count_last)

N, M = map(int, input().split())
board = []

for i in range(N):
    board.append(input())

min_count = N * M + 1
for i in range(N):
    for j in range(M):
        if i + 8 > N or j + 8 > M:
            continue
        else:
            result = check_board(board, i, j)
            if min_count > result:
                min_count = result

print(min_count)
