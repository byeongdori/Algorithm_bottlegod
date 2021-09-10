# 2020 KAKAO BULID RECRUITMENT
# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    max_divide_length = int(len(s) / 2)
    answer = len(s)
    for i in range (1, max_divide_length + 1):
        if answer > compress_string(i, s):
            answer = compress_string(i, s)
    return answer

# 문자열 압축시 압축된 길이 반환하는 함수
def compress_string(divide_length, input_str):
    str_len = len(input_str)
    if str_len == 1:
        return 1

    count = 1
    compress_str = ''
    divide_str = input_str[:divide_length]

    # for문의 마지막 조건, divide_length 만큼 단계 건너 뜀!
    for i in range (divide_length, str_len, divide_length):
        if input_str[i:i+divide_length] == divide_str:
            count += 1
        else:
            if count != 1:
                compress_str = compress_str + str(count) + divide_str
            else:
                compress_str = compress_str + divide_str
            divide_str = input_str[i:i+divide_length]
            count = 1
    if count != 1:
        compress_str = compress_str + str(count) + divide_str
    else:
        compress_str = compress_str + divide_str
    return len(compress_str)
