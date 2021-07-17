# 2839

a = int(input())
temp = 9999
for i in range(0, 1001):
    for j in range(0, 1700):
        if 5 * i + 3 * j == a and i + j < temp:
            temp = i + j

if temp == 9999:
    temp = -1
print(temp)