# 14888 - 연산자 끼워넣기
# 모든 경우의 수 고려 - DFS

n = int(input())
num_arr = list(map(int, input.split()))
op_arr= list(map(int, input.split()))

def test(plus, minus, multi, divide, current_sum):
    # 연산자 다 쓴 경우, 최대/최소 계산
    # 재귀 종료 시점

    # 연산자 남아있는 경우, DFS
    if plus > 0:
        pass
    if minus > 0:
        pass
    if multi > 0:
        pass
    if divide > 0:
        pass