# 14889 - 스타트와 링크
        
import sys
sys.setrecursionlimit(10000)

def dfs(idx, cnt):
    global answer
    # 팀 나눈 경우, 점수 차이 계산
    if cnt == N // 2:
        team_1 = 0
        team_2 = 0
        for i in range(N):
            for j in range(N):
                if visited[i] == 0 and visited[j] == 0:
                    team_1 += arr[i][j]
                elif visited[i] == 1 and visited[j] == 1:
                    team_2 += arr[i][j]
        answer = min(answer, abs(team_1 - team_2))
    
    # 팀 나누기
    for i in range(idx, N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        dfs(i + 1, cnt + 1)
        visited[i] = 0

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
visited = [0 for _ in range (N)]
answer = sys.maxsize

dfs(0, 0)
print(answer)
