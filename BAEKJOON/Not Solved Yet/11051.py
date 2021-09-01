# 11051 - 이항계수 2
# 이항계수의 성질 & 다이나믹 프로그래밍
# nCr = n-1Cr-1 + n-1Cr

input_spilt = input().split()

n = int(input_spilt[0])
k = int(input_spilt[1])

# n, k 행 열로 가지는 2차원 배열로 생성
Combarr = []

