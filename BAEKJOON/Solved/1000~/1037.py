# 1037 - 약수

n = int(input())
num = list(map(int, input().split()))
num.sort()

if len(num) == 1:
    print(num[0] * num[0])
else:
    print(num[0] * num[len(num) - 1])
