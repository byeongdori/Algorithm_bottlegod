# 1806 - 부분합
# 투 포인터
# 합을 구한 배열을 만들어서 다시 짜기
import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))
min_len = sys.maxsize
start, end = 0, 1

temp = arr[start] + arr[end]
while start < end:
    if temp == S:
        len = end - start + 1
        if min_len > len:
            min_len = len
        end += 1
        temp += arr[end]
    elif temp < S:
        if start + 1 == end:
            if end 
            end += 1
            temp += arr[end]
        else:
            temp -= arr[start]
            start += 1
    else:
        temp -= arr[start]
        start += 1

print(min_len)
        