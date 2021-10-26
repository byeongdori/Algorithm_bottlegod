# 1197 - 최소 스패닝 트리
# 크루스칼 알고리즘 참고하기

V, E = map(int, input().split())

graph = []
visit = [0 for _ in range(V + 1)]
answer = 0 

for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

graph.sort(key = lambda x:x[2])

for i in graph:
    if visit[i[1]] == 0:
        visit[i[0]] = 1
        visit[i[1]] = 1
        answer += i[2]

    if sum(visit) == V:
        break

print(answer)

