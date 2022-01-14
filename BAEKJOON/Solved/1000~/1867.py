# 1867 - 돌맹이 제거
# 이분 매칭, 최소 버텍스 커버

import sys

def find_minimum_vertex_cover(index):
    # 이미 방문한 정점인 경우, 함수 종료
    if visit[index] == 1:
        return 0
    
    # 방문 진행
    visit[index] = 1
    for i in stone[index]:
        if answer[i] == 0 or find_minimum_vertex_cover(answer[i]):
            answer[i] = index
            return 1
    
    return 0

N, K = map(int, input().split())
stone = [[] for _ in range(N + 1)]
answer = [0 for _ in range(N + 1)]

for _ in range(K):
    n, m = map(int, sys.stdin.readline().split())
    stone[n].append(m)

for i in range(1, N + 1):
    visit = [0 for i in range(N + 1)]
    find_minimum_vertex_cover(i)

print(len(answer) - answer.count(0))

            
    