# 실패율
# 2019 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

def solution(N, stages):
    answer = []
    culmul_stage = [0 for _ in range(N + 2)]
    current_stage = [0 for _ in range(N + 2)]
    for i in stages:
        current_stage[i] += 1
        for j in range(1, i + 1):
            culmul_stage[j] += 1

    fail_rate = []
    for i in range(1, N + 1):
        if culmul_stage[i] == 0:
            fail_rate.append([i, 0])
        else:
            fail_rate.append([i, current_stage[i] / culmul_stage[i]])
    fail_rate.sort(key = lambda x: x[1], reverse=True)
    
    for i in range(0, N):
        answer.append(fail_rate[i][0])
    return answer