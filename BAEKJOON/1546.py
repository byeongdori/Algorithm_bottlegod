# 1546 - 평균

totalnum = int(input())

input_split = input().split()
score = list(map(int, input_split))

score.sort()
max_score = score[totalnum - 1]
new_score = [x / max_score * 100 for x in score]

total_score = 0
for x in new_score:
    total_score += x

print(total_score / totalnum)