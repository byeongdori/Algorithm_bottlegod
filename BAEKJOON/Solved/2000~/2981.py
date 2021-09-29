# 2981 - 검문
# a[i] - a[i - 1]의 최대공약수 구하기
# 최대공약수 효율적으로 구하기

import math

num_count = int(input())

input_num = []
for i in range(num_count):
    input_num.append(int(input()))
input_num.sort()

arr = []
for i in range(num_count - 1):
    arr.append(input_num[i + 1] - input_num[i])

gcd = arr[0]
for i in range(1, len(arr)):
    gcd = math.gcd(gcd, arr[i])

answer = []
for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        answer.append(i)
        # // 나눗셈은 결과가 int
        answer.append(gcd // i)
answer.append(gcd)

answer = list(set(answer))
answer.sort()

print(*answer)

