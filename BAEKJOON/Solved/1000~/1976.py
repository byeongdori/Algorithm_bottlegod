# 1976 - 여행 가자
# Disjoint Set

def parent_find(x):
    if parent[x] == x:
        return x
    else:
        return parent_find(parent[x])

def union(x, y):
    x = parent_find(x)
    y = parent_find(y)

    if x != y:
        parent[x] = y
        
N = int(input())
M = int(input())

# 부모를 자기자신으로 초기화
parent = [0 for _ in range(N + 1)]
for i in range(N + 1):
    parent[i] = i

# 자식 - 부모 연결
for i in range(1, N + 1):
    graph = list(map(int, input().split()))
    for j in range(len(graph)):
        if graph[j] == 1:
            union(i, j + 1)

# 하나씩 부모를 찾으면서, 연결되어 있는지 확인
# 모두 부모가 같다면, 연결되어있는것!
visit = list(map(int, input().split()))
result = set(parent_find(x) for x in visit)
if len(result) != 1:
    print("NO")
else:
    print("YES")