# 2533 - 사회망 서비스(SNS)

import sys
sys.setrecursionlimit(10**9)

def dfs(n):
    visit[n] = True
    dp[n][0] = 0
    dp[n][1] = 1
    for i in tree[n]:
        if visit[i] == False:
            dfs(i)
            dp[n][0] += dp[i][1]
            dp[n][1] += min(dp[i][0], dp[i][1])

N = int(input())

tree = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
# dp[i] -> i 번째 노드에서의 얼리어답터의 수 저장
# dp[i][0] -> i 번째 사람이 얼리어답터가 아닌 경우
# dp[i][1] -> i 번째 사람이 얼리어답터인 경우
dp= [[0 for _ in range(2)] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
print(min(dp[1][0], dp[1][1]))