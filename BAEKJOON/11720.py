# 11720 - 숫자의 합
# 큰 수 나눗셈하면, 오버플로우 날 수도 있음

total_num = int(input())
input_num = input()
temp = int(input_num)
sum_of_num = 0

for i in range(0, total_num):
    sum_of_num += int(input_num[i])

print(sum_of_num)
