# 2579 - 계단 오르기
# 다이나믹 프로그래밍, 동적 계획법

# 마지막 계단 기준 점화식
# total[n] = score[n] + score[n-1] + total[n-3]
# total[n] = score[n] + total[n-2]

num_of_step = int(input())
score_of_step = [0 for i in range (num_of_step + 1)]
max_score_of_current_step = [0 for i in range (num_of_step + 1)]

for i in range(0, num_of_step):
    score_of_step[i] = int(input())

max_score_of_current_step[0] = score_of_step[0]
max_score_of_current_step[1] = max_score_of_current_step[0] + score_of_step[1]
max_score_of_current_step[2] = max(score_of_step[0]+score_of_step[2], score_of_step[1]+score_of_step[2])

for i in range(3, num_of_step):
    max_score_of_current_step[i] = score_of_step[i] + max(score_of_step[i-1]+max_score_of_current_step[i-3],max_score_of_current_step[i-2])

print(max_score_of_current_step[num_of_step - 1])