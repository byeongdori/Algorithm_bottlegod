# 2020 카카오 인턴십
# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    current_left, current_right = 0, 0
    answer = []
    for i in numbers:
        if i % 3 == 1:
            answer.append("L")
            current_left = i
        elif i % 3 == 0:
            answer.append("R")
            current_right = i
        else:
            pass
            # 양쪽 거리 계산
    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))