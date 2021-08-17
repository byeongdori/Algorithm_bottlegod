# 2020 KAKAO BULID RECRUITMENT
# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059
# key 배열에 제로 패딩 추가해서 완전 탐색

# 배열 인덱스 체크
def solution(key, lock):
    # 제로 패딩 추가
    new_lock_len = len(lock) + 2*(len(key) - 1)
    new_lock =[[0 for i in range(0, new_lock_len)] for i in range (0, new_lock_len)]
    for i in range(len(key) - 1, new_lock_len - (len(key) - 1)):
        for j in range(len(key) - 1, new_lock_len - (len(key) - 1)):
            new_lock[i][j] = lock[i-2][j-2]

    # 검사
    for i in range(0, new_lock_len):
        for j in range(0, new_lock_len):
            pass
    
    answer = True
    return answer

def rotate(key):
    pass

# lock 배열 값 변경 되지 않는가?
def check(key, key_start_i, key_start_j, lock):
    for i in range(0, len(key)):
        for j in range(0, len(key)):
            if (key_start_i + i >= 2) and (key_start_i + i <= 4) and (key_start_j + j >= 2) and (key_start_j + j <= 4):
                lock[key_start_i + i][key_start_j + j] += key[key_start_i + i][key_start_j + j] 
    
    for i in range(len(key) - 1, len(lock) - (len(key) + 1)):
        for j in range(len(key) - 1, len(lock) - (len(key) + 1)):
            if lock[i][j] > 1 or lock[i][j] == 0:
                return False
    
    return True