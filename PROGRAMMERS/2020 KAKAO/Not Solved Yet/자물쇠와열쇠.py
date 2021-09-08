# 2020 KAKAO BULID RECRUITMENT
# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059
# key 배열에 제로 패딩 추가해서 완전 탐색
# attach / detach 인덱스 체크

def solution(key, lock):
    # 제로패딩 추가한 board 배열 생성 및 초기화
    key_len, lock_len = len(key), len(lock)
    board_len = key_len * 2 + lock_len
    board_arr = [[0] * board_len for _ in range(board_len)]

    for i in range (key_len, board_len - key_len):
        for j in range (key_len, board_len - key_len):
            board_arr[i][j] = lock[i - key_len][j - key_len]
    
    # 함수 이용해 자물쇠 맞춰보기
    for _ in range (4):
        for i in range (1, board_len - key_len):
            for j in range (1, board_len - key_len):
                attach(i, j, key, board_arr)
                if check(key_len, board_arr):
                    return print("true")
                detach(i, j, key, board_arr)
        key = rotate(key)

    return print("false")

# key 회전
def rotate(key):
    return list(zip(*key[::-1]))

# key와 자물쇠 결합
def attach(x, y, key, board):
    key_len = len(key)
    for i in range (x, x+key_len):
        for j in range (y, y+key_len):
            board[i][j] = board[i][j] + key[i - x][j- y]
    return board

# key와 자물쇠 해제
def detach(x, y, key, board):
    key_len = len(key)
    for i in range (x, x+key_len):
        for j in range (y, y+key_len):
            board[i][j] = board[i][j] - key[i - x][j- y]
    return board

# 풀렸는지 체크하는 함수
def check(key_len, board):
    board_len = len(board)
    for i in range (key_len, board_len - key_len):
        for j in range (key_len, board_len - key_len):
            # print(board[i][j])
            if board[i][j] == 0:
                # print("###")
                return False
    return True
'''
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(key, lock)
'''