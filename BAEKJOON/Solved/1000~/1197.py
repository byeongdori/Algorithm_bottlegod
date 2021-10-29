# 1197 - 최소 스패닝 트리
# 크루스칼 알고리즘 참고하기

import sys

def find_parent(n):
    if n == parent[n]:
        return n
    else:
        return find_parent(parent[n])


V, E = map(int, input().split())

graph = []
parent = [i for i in range(V + 1)]
answer = 0 

for _ in range(E):
    graph.append(list(map(int, sys.stdin.readline().split())))

graph.sort(key = lambda x:x[2])

for a, b, c in graph:
    a_parent = find_parent(a)
    b_parent = find_parent(b)    

    if a_parent == b_parent:
        continue
    else:
        if a_parent < b_parent:
            parent[a_parent] = b_parent
        else:
            parent[b_parent] = a_parent
        answer += c

print(answer)

