# 2798 - 블랙잭

input_split = input().split()

num_of_card = int(input_split[0])
total_sum = int(input_split[1])
current_max_sum = 0

card_num = list(map(int, input().split()))
card_num.sort()

for i in range(0, len(card_num)):
    for j in range(i+1, len(card_num)):
        for k in range(j+1, len(card_num)):
            sum = card_num[i] + card_num[j] + card_num[k]
            if sum > current_max_sum and sum <= total_sum:
                current_max_sum = sum

print(current_max_sum)