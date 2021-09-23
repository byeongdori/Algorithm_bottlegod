# 2805 - 나무 자르기
# 이분 탐색, 조건 추가해서 필요없는 탐색 줄이기

input_split = input().split()
n, m = int(input_split[0]), int(input_split[1])
tree = list(map(int, input().split()))
tree.sort()
tree.reverse()

low, high = 1, max(tree) - 1

while low <= high:
    middle = (low + high) // 2
    total_length = 0
    for i in tree:
        if i > middle:
            total_length += i - middle
            if total_length >= m:
                break
        else:
            break

    if total_length >= m:
        low = middle + 1
    else:
        high = middle - 1

print(high)
