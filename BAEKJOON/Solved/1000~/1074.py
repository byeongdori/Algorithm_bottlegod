# 1074 - Z

# i -> 행, j -> 열
def findZ(i, j, current_length):
    global cnt
    if i == r and j == c:
        print(cnt)
        exit(0)
    elif current_length == 1:
        cnt += 1
        return
    # 재귀함수 시간 줄이기!
    if not (i <= r < i + current_length) and not (j <= c < j + current_length):
        cnt += current_length ** 2
        return  

    findZ(i, j, current_length // 2)
    findZ(i, j + current_length // 2, current_length // 2)
    findZ(i + current_length // 2, j, current_length // 2)
    findZ(i + current_length // 2, j + current_length // 2, current_length // 2)

N, r, c = map(int, input().split())
length = pow(2, N)
cnt = 0
findZ(0, 0, length)