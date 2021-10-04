# 3273 - 두 수의 합
# 투 포인터

size = int(input())
num = list(map(int, input().split()))
sum = int(input())
num.sort()

count, left, right = 0, 0, len(num) - 1

while left < right:
    temp = num[left] + num[right]
    if temp > sum:
        right -= 1
    elif temp < sum:
        left += 1
    else:
        count += 1
        left += 1

print(count)