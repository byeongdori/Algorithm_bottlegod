# 13305 - 주유소
# 그리디 알고리즘

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

current = 0
total_cost = 0
temp = current + 1

while current < n - 1:
    if price[current] > price[temp] or temp == n - 1:
        distance = 0
        for i in range(current, temp):
            distance += road[i]
        total_cost += price[current] * distance
        current = temp
        temp = current + 1
    else:
        temp += 1
    

print(total_cost)