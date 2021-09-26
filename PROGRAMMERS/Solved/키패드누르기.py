# 2020 카카오 인턴십
# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    current_left, current_right = 10, 12
    answer = []
    for i in numbers:
        if i % 3 == 1:
            answer.append("L")
            current_left = i
        elif i % 3 == 0 and i != 0:
            answer.append("R")
            current_right = i
        else:
            if current_left == 0:
                current_left = 11
            if current_right == 0:
                current_right = 11
            if i == 0:
                i = 11

            distance_left = abs((i - 1) // 3  - (current_left - 1) // 3)
            distance_right = abs((i - 1) // 3  - (current_right - 1) // 3)
            if current_left % 3 != i % 3:
                distance_left += 1
            if current_right % 3 != i % 3:
                distance_right += 1
            print(i, distance_left, distance_right)
            if distance_left > distance_right:
                answer.append("R")
                current_right = i
            elif distance_left < distance_right:
                answer.append("L")
                current_left = i
            else:
                if hand == "left":
                    answer.append("L")
                    current_left = i
                else:
                    answer.append("R")
                    current_right = i
    answer = "".join(answer)
    return answer

numbers = [1,2,3,4,5,6,7,8,9,0]
hand = "right"
print(solution(numbers, hand))