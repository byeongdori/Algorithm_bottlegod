# https://programmers.co.kr/learn/courses/30/lessons/42895
# N으로 표현

def solution(N, number):

    numbers = set()
    # k개의 N으로 만들수 있는 수

    # k개의 N을 단순하게 잇거나, 
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

    # k-1개의 결과를 k와 사칙연산한 결과
    #   { 
    #       "n" * i U 
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set, 
    #    } 
    answer = 0
    return answer
