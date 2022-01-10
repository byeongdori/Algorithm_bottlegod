# 멀쩡한 사각형
# Summer/Winter Coding(2019)
# https://programmers.co.kr/learn/courses/30/lessons/62048
# 최대 공약수가 1이면, 가로 + 세로 - 1이 잘려진 사각형의 개수!

import math

def solution(w,h):
    gcd = math.gcd(w, h)
    return w * h - (w + h - gcd)