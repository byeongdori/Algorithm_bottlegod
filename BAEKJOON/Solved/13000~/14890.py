# 14890 - 경사로

N, L = map(int, input().split())
roadmap = []
for _ in range(N):
    roadmap.append(list(map(int, input().split())))
answer = 0

def check_horizonal(index):
    global answer
    visited = [False for _ in range(N)]

    for j in range(N - 1):
        # 높이 차이가 2이상이면 끝
        if abs(roadmap[index][j] - roadmap[index][j + 1]) > 1:
            return
            
        # 오르막
        if roadmap[index][j] < roadmap[index][j + 1]:
            if j + 1 - L < 0:
                return
            temp = roadmap[index][j + 1 - L]
            for k in range(j + 1 - L, j + 1):
                if temp != roadmap[index][k] or visited[k] == True:
                    return
            for k in range(j + 1 - L, j + 1):
                visited[k] = True

        # 내리막
        if roadmap[index][j] > roadmap[index][j + 1]:
            temp = roadmap[index][j + 1]
            for k in range(j + 1, j + 1 + L):
                if k >= N or temp != roadmap[index][k]:
                    return
            for k in range(j + 1, j + 1 + L):
                visited[k] = True
    #print("hori", index)
    answer += 1

def check_vertical(index):
    global answer
    visited = [False for _ in range(N)]
    for j in range(N - 1):
        # 높이 차이가 2이상이면 끝
        if abs(roadmap[j][index] - roadmap[j + 1][index]) > 1:
            return

        # 오르막
        if roadmap[j][index] < roadmap[j + 1][index]:
            if j + 1 - L < 0:
                return
            temp = roadmap[j + 1 - L][index]
            for k in range(j + 1 - L, j + 1):
                if temp != roadmap[k][index] or visited[k] == True:
                    return
            for k in range(j + 1 - L, j + 1):
                visited[k] = True            

        # 내리막
        if roadmap[j][index] > roadmap[j + 1][index]:
            temp = roadmap[j + 1][index]
            for k in range(j + 1, j + 1 + L):
                if k >= N or temp != roadmap[k][index]:
                    return
            for k in range(j + 1, j + 1 + L):
                visited[k] = True 
    answer += 1

for i in range(N):
    check_horizonal(i)
    check_vertical(i)

print(answer)