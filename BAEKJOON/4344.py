# 4344
# 파이썬 리스트 원소를 좀 더 자유자재로 다룬다면 더 줄일수도 있을듯

test_case = int(input())
temp = 0
score_arr = []

while (temp < test_case):
    input_spilt = input().split()
    students = int(input_spilt[0])
    temp_2 = 0
    total_score = 0
    while (temp_2 < students):
        score_arr.insert(temp_2, int(input_spilt[temp_2 + 1]))
        total_score = total_score + score_arr[temp_2]
        temp_2 = temp_2 + 1

    temp_2 = 0
    count = 0
    avg_score = total_score / students

    while (temp_2 < students):
        if score_arr[temp_2] > avg_score:
            count = count + 1
        temp_2 = temp_2 + 1

    count = (count / students) * 100
    print("{:.3f}%".format(count))
    temp = temp + 1
