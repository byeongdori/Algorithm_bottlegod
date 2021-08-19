# 2579 - 계단 오르기
# 다이나믹 프로그래밍, 동적 계획법

# 동적 배열을 어떻게 저장해야 하는가? 
# 최대인 위치 계산 시, 직전에 몇칸을 뛰었는지 판단해야함
# 직전에 몇칸 뛰었는지 판단하는 변수 필요
num_of_step = int(input())
score_of_step = []
max_score_of_current_step = []

for i in range(0, num_of_step):
    score_of_step.append(int(input()))

print(score_of_step) 

