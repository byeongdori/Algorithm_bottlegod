# 2630 - 색종이 만들기
# 분할정복, 재귀

size = int(input())
paper = []

white_paper = 0
blue_paper = 0

for i in range(size):
    paper.append(list(map(int, input().split())))

def check_paper(paper, x, y, size):
    global white_paper, blue_paper

    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                check_paper(paper, x, y, size //2)
                check_paper(paper, x + size // 2, y, size // 2)
                check_paper(paper, x, y + size // 2, size // 2)
                check_paper(paper, x + size // 2, y + size // 2, size // 2)
                return
    
    if color == 0:
        white_paper += 1
        return
    else:
        blue_paper += 1
        return

check_paper(paper, 0, 0, size)
print(white_paper)
print(blue_paper)