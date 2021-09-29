# 4673 - 셀프 넘버(Self Number)

mark = []
for i in range(10001):
    mark.append(0)

def self_number(num):
    result = num
    while num >= 10:
        result += num % 10
        num = int(num / 10)
    result += num
    return result


for i in range(1, 10000):
    temp = self_number(i)
    while temp <= 10000:
        mark[temp] = 1
        temp = self_number(temp)

for i in range(1, 10000):
    if mark[i] == 0:
        print(i)
