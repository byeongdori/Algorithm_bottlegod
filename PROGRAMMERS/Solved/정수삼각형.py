# 정수 삼각형
# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):

    size = len(triangle)
    max_sum = [[0 for i in range(size)] for j in range(size)]
    max_sum[0][0] = triangle[0][0]

    for i in range(1,size):
        for j in range(0, i + 1):
            if j == 0:
                max_sum[i][j] = triangle[i][j] + max_sum[i - 1][j]
            elif j == i:
                max_sum[i][j] = triangle[i][j] + max_sum[i - 1][j - 1]
            else:
                max_sum[i][j] = triangle[i][j] + max(max_sum[i - 1][j - 1], max_sum[i - 1][j])

    return max(max_sum[size - 1])
