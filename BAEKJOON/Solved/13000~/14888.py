# 14888 - 연산자 끼워넣기
# 모든 경우의 수 고려 - DFS
import sys

n = int(input())
num_arr = list(map(int, input().split()))
op_arr = list(map(int, input().split()))

current_cal = num_arr[0]
result_max = - sys.maxsize - 1
result_min = sys.maxsize

def calculate_dfs(index, plus, minus, multi, divide, current_cal):

    # 연산자 다 쓴 경우, 최대/최소 계산
    # 재귀 종료 시점
    if index == n:
        global result_max
        global result_min

        if current_cal > result_max:
            result_max = current_cal
        if current_cal < result_min:
            result_min = current_cal
        return

    # 연산자 남아있는 경우, DFS
    if plus > 0:
        calculate_dfs(index + 1, plus - 1, minus, multi, divide, current_cal + num_arr[index])
    if minus > 0:
        calculate_dfs(index + 1, plus, minus - 1, multi, divide, current_cal - num_arr[index])
    if multi > 0:
        calculate_dfs(index + 1, plus, minus, multi - 1, divide, current_cal * num_arr[index])
    if divide > 0:
        calculate_dfs(index + 1, plus, minus, multi, divide - 1, int(current_cal / num_arr[index]))

calculate_dfs(1, op_arr[0], op_arr[1], op_arr[2], op_arr[3], current_cal)

print(result_max)
print(result_min)