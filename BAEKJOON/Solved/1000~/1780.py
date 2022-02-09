# 1780 - 종이의 개수
# 분할 정복

import sys

N = int(input())

def check_paper(x, y, size):

    color = paper[x][y]
    temp = size // 3
    if size > 1:
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] != color:
                    # 분할
                    check_paper(x, y, temp)
                    check_paper(x, y + temp, temp)
                    check_paper(x, y + temp * 2, temp)
                    check_paper(x + temp, y, temp)
                    check_paper(x + temp, y + temp, temp)
                    check_paper(x + temp, y + temp * 2, temp)
                    check_paper(x + temp * 2, y, temp)
                    check_paper(x + temp * 2, y + temp, temp)
                    check_paper(x + temp * 2, y + temp * 2, temp)
                    return

    if paper[x][y] == -1:
        answer[0] += 1
    elif paper[x][y] == 0:
        answer[1] += 1
    else:
        answer[2] += 1
    
paper = []
for _ in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))

answer = [0, 0, 0]
check_paper(0, 0, N)

for a in answer:
    print(a)
