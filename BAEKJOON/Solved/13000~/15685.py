# 15685 - 드래곤 커브

import sys,copy

N = int(input())
curve = []
for _ in range(N):
    curve.append(list(map(int, sys.stdin.readline().split())))

array = [[0 for _ in range(101)] for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    genelist = []
    genelist.append(curve[i][2])

    # N 세대만큼의 방향 genelist에 저장
    for j in range(1, curve[i][3] + 1):
        temp = copy.deepcopy(genelist)
        temp.reverse()
        for k in range(len(temp)):
            temp[k] = (temp[k] + 1) % 4
        genelist = genelist + temp

    # 드래곤 커브의 결과 배열에 Mapping
    current = [curve[i][1], curve[i][0]]
    array[current[0]][current[1]] = 1
    for j in genelist:
        current = [current[0] + dy[j], current[1] + dx[j]]
        if current[0] <= 100 and current[0] >= 0 and current[1] >= 0 and current[1] <= 100:
            array[current[0]][current[1]] = 1

# 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것 찾기
answer = 0
for i in range(100):
    for j in range(100):
        if array[i][j] == 1 and array[i][j + 1] == 1 and array[i + 1][j] == 1 and array[i + 1][j + 1] == 1:
            answer += 1

print(answer)
