# 15652 - N과 M (4)
# 1~N개까지의 자연수 중에서 M개 선택하여 출력 / 비내림차순 / 중복허용
# 백트래킹

input_split = input().split()

n = int(input_split[0])
m = int(input_split[1])

output = []

def back_tracking(n, m, current, loop):

    # 재귀 종료 조건
    if loop == m:
        print(*output)

    # 재귀 내부
    for i in range (current, n):
        output.append(i)
        back_tracking(n, m, current, loop + 1)
        output.pop()

back_tracking(n, m, 1, 1)