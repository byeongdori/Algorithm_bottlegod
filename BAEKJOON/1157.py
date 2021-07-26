# 1157 - 단어 공부

# 입력 받아서 중복 제거해 리스트 생성
string_input = input().lower()
string_unique = list(set(string_input))
count_list = []

# 중복되는 단어 개수 세기
for i in string_unique:
    count = string_input.count(i)
    count_list.append(count)

# 출력
if count_list.count(max(count_list)) >= 2:
    print("?")
else:
    print(string_unique[count_list.index(max(count_list))].upper())
