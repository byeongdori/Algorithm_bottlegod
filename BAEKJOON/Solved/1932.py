# 1932 - 정수 삼각형
# 다이나믹 프로그래밍(동적 계획법)
# 최댓값 동적으로 저장하여 사용

size = int(input())
triangle = []
max_sum = [[0 for i in range(size)] for j in range(size)]

for i in range(size):
    triangle.append(list(map(int, input().split())))

max_sum[0][0] = triangle[0][0]

for i in range(1,size):
    for j in range(0, i + 1):
        if j == 0:
            max_sum[i][j] = triangle[i][j] + max_sum[i - 1][j]
        elif j == i:
            max_sum[i][j] = triangle[i][j] + max_sum[i - 1][j - 1]
        else:
            max_sum[i][j] = triangle[i][j] + max(max_sum[i - 1][j - 1], max_sum[i - 1][j])

print(max(max_sum[size - 1]))