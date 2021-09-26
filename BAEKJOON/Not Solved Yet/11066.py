# 11066 - 파일 합치기
# 동적 계획법(다이나믹 프로그래밍)
# Knuth's Optimization 생각해서 다시 풀기

case = int(input())

for i in range (case):
    k = int(input())
    dp = [[0 for _ in range(k + 1)] for _ in range(k + 1)]
    size = list(map(int, input().split()))

    for j in range(k):
        dp[j][j] = size[j]

    count = k - 1
    for j in range(k):
        for p in range(0,count):
            dp[p][p + j] = min(size[p] + dp[p+1][p+j], dp[p][p+j-1]+size[p+j])
            print(j, p, dp[j][p])
        count -= 1
    print(dp[0][k-1])