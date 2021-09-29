# 11051 - 이항계수 2
# 이항계수의 성질 & 다이나믹 프로그래밍
# nCr = n-1Cr-1 + n-1Cr

input_spilt = input().split()

n = int(input_spilt[0])
k = int(input_spilt[1])

# n, k 행 열로 가지는 2차원 배열로 생성
Combi = [[1 for i in range(n + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1:
            Combi[i][j] = i
        elif j == i:
            Combi[i][j] = 1
        else:
            Combi[i][j] = Combi[i-1][j-1] + Combi[i-1][j]

print(Combi[n][k] % 10007)