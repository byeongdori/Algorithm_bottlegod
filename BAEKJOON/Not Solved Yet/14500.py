# 14500 - 테트로미노

# 배열 인덱스 오류, 가로 인덱스 체크하기!

# 가로 모양
def tetris_1(i, j, M, poly):

    if j + 3 > M:
        return -1
    
    sum = 0
    for k in range(4):
        sum += poly[i][j + k]
    return sum

# 정사각형 모양
def tetris_2(i, j, N, M, poly):

    if i + 1 > N or j + 1 > M:
        return -1
    
    sum = 0
    for k in range(2):
        for l in range(2):
            sum += poly[i + k][j + l]
    return sum

# L자 모양
def tetris_3(i, j, N, M, poly):

    if i + 2 > N or j + 1 > M:
        return -1

    return poly[i][j] + poly[i + 1][j] + poly[i + 2][j] + poly[i + 2][j + 1]

# ㄴ, ㄱ 합친 모양
def tetris_4(i, j, N, M, poly):
    
    if i + 2 > N or j + 1 > M:
        return -1
    
    return poly[i][j] + poly[i + 1][j] + poly[i + 1][j + 1] + poly[i + 2][j + 1]
    
# ㅜ 모양
def tetris_5(i, j, N, M, poly):
    
    if i + 1 > N or j + 2 > M:
        return -1
    
    return poly[i][j] + poly[i][j + 1] + poly[i][j + 2] + poly[i + 1][j + 1]

N, M = map(int, input().split())

answer = -1
poly = [[]]

for _ in range(N):
    poly.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(0, M):
        answer = max(answer, tetris_1(i, j, M, poly), tetris_2(i, j, N, M, poly), tetris_3(i, j, N, M, poly), tetris_4(i, j, N, M, poly), tetris_5(i, j, N, M, poly))

print(answer)