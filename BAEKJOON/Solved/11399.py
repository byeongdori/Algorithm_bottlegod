# 11399 - ATM
# 그리디 알고리즘, 정렬

num_of_people = int(input())

time_arr = list(map(int, input().split()))
time_arr.sort()

total_spent_time = 0

for i in range(0, num_of_people):
    total_spent_time += time_arr[i] * (num_of_people - i)

print(total_spent_time)