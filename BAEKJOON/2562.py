# 2562 - 최댓값 

input_split = []
for i in range(0, 9):    
    input_split.append(int(input()))

max_num = 0
max_index = 0

for i in range (0, len(input_split)):
    if input_split[i] > max_num:
        max_num = input_split[i]
        max_index = i

print(max_num)
print(max_index + 1) 
