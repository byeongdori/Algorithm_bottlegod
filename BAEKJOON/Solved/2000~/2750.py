# 2750 - 수 정렬하기

count_of_num = int(input())
num_list = []

for i in range(0, count_of_num):
    num_list.append(int(input()))

num_list.sort()

for i in range(0, count_of_num):
    print(num_list[i])