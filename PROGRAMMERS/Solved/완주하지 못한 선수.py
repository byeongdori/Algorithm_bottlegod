# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
# 완주하지 못한 선수
# 해시, 효율성 - 완주하지 못한 선수는 단 한명
# zip 함수 - 같은 인덱스끼리 짝지어줌!

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()