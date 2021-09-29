# 11047 - 동전 0
# 빠른 입출력 사용

import sys

input_split = input().split()
n = int(input_split[0])
k = int(input_split[1])

coin_value = []

for i in range (n):
    coin_value.append(int(sys.stdin.readline()))

coin_num = 0
i = 0
while k > 0:
    if k >= coin_value[n - i - 1]:
        coin_num += int(k / coin_value[n - i - 1])
        k = k % coin_value[n - i - 1]
    elif k < coin_value[n - i - 1]:
        i += 1

print(coin_num)