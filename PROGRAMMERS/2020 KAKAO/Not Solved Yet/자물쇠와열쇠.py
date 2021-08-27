# 2020 KAKAO BULID RECRUITMENT
# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059
# key 배열에 제로 패딩 추가해서 완전 탐색


def solution(key, lock):
    # 제로패딩 추가한 board 배열 생성 및 초기화
    key_len, lock_len = len(key), len(lock)
    board_len = key_len * 2 + lock_len
    board_arr = [[0 for i in range(board_len)] for i in range(board_len)]

    for i in range (key_len, board_len - key_len):
        for j in range (key_len, board_len - key_len):
            board_arr[i][j] = lock[i - key_len][j - key_len]

def rotate(key):
    pass

def attach(x, y):
    pass

def detach(x, y):
    pass

def check():
    pass