# 4354 - 문자열 제곱
# KMP 알고리즘
# 실패함수 구현하는 부분 다시보기
import sys

while 1: 
    temp = sys.stdin.readline().rstrip()
    if temp == ".":
        break
    fail = [0] * len(temp)
    begin, j = 1, 0
    for i in range(1, len(temp)):
        while j > 0 and temp[i] != temp[j]:
            j = fail[j - 1]
        if temp[i] == temp[j]:
            j += 1
            fail[i] = j
    '''
    while begin + m < len(temp):
        if temp[m] == temp[m + begin]:
            m += 1
            fail[m + begin - 1] = m
        else:
            if m == 0:
                begin += 1
            else:
                begin += m - fail[m - 1]
                m = fail[m -1]
    '''
    if len(temp) % (len(temp) - fail[-1]) == 0:
        print(int(len(temp) / (len(temp) - fail[-1])))
    else:
        print(1)