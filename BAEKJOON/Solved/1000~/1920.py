# 1920 - 수 찾기
# 이분 탐색

n = int(input())
num_arr = list(map(int, input().split()))
num_arr.sort()

k = int(input())
check_arr = list(map(int, input().split()))

def binary_search(arr, num):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        middle = (start + end) // 2
        if arr[middle] == num:
            return 1
        elif arr[middle] < num:
            start = middle + 1
        else:
            end = middle - 1
    return 0

for i in check_arr:
    print(binary_search(num_arr, i))