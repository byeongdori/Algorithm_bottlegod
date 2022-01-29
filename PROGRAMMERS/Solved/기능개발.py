# https://programmers.co.kr/learn/courses/30/lessons/42586
# 기능개발

def solution(progresses, speeds):
    answer = []
    temp = 1
    result = 0

    while progresses:
        p, s = progresses[0], speeds[0]

        if p + temp * s >= 100:
            progresses.pop(0)
            speeds.pop(0)
            result += 1
        else:
            if result > 0:
                answer.append(result)
                result = 0
            temp += 1
    answer.append(result)
    return answer
