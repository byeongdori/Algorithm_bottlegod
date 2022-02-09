# 7568 - 덩치
# 브루트포스

import sys

n = int(input())
people = []
for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))

answer = [0] * n
for i in range(n):
    weight, height = people[i][0], people[i][1]
    for j in range(n):
        if people[j][0] > weight and people[j][1] > height:
            answer[i] += 1

for a in answer:
    print(a + 1)
