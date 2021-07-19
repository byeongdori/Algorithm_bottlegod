# 10818 - 최소, 최대

num = int(input())
array = []
input_split = input().split()
for i in range(0,num):
    array.append(int(input_split[i]))

array.sort()
print(array[0], array[num-1])
