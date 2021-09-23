# 2020 KAKAO BULID RECRUITMENT
# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059
# key 배열에 제로 패딩 추가해서 완전 탐색
# attach / detach 인덱스 체크

def solution(key, lock):
    # 제로패딩 추가한 board 배열 생성 및 초기화
    key_len, lock_len = len(key), len(lock)
    board_len = key_len * 2 + lock_len
    board_arr = [[0] * board_len for _ in range (board_len)]

    for i in range (lock_len):
        for j in range (lock_len):
            board_arr[key_len + i][key_len + j] = lock[i][j]
    
    # 함수 이용해 자물쇠 맞춰보기
    for _ in range (4):
        for i in range (1, key_len + lock_len):
            for j in range (1, key_len + lock_len):
                attach(i, j, key, board_arr)
                if check(key_len, lock_len, board_arr):
                    return True
                detach(i, j, key, board_arr)
        key = rotate(key)
    return False

# key 회전
def rotate(key):
    return list(zip(*key[::-1]))

# key와 자물쇠 결합
def attach(x, y, key, board):
    for i in range (len(key)):
        for j in range (len(key)):
            board[i + x][j + y] += key[i][j]
    return board

# key와 자물쇠 해제
def detach(x, y, key, board):
    for i in range (len(key)):
        for j in range (len(key)):
            board[i + x][j + y] -= key[i][j]
    return board

# 풀렸는지 체크하는 함수
def check(key_len, lock_len, board):
    for i in range (lock_len):
        for j in range (lock_len):
            if board[key_len+i][key_len+j] != 1:
                return False
    return True

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(key, lock)