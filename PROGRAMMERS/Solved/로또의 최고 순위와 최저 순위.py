# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    zero = 0
    correct = 0

    for i in lottos:
        if i == 0:
            zero += 1
    
    for i in range(zero, 6):
        for j in range(0, 6):
            if lottos[i] == win_nums[j]:
                correct += 1
                continue

    max_rank = 7 - (correct + zero)
    min_rank = 7 - correct

    if max_rank == 7:
        max_rank = 6
    if min_rank == 7:
        min_rank = 6
        
    answer = []
    answer.append(max_rank)
    answer.append(min_rank)
    return answer

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))