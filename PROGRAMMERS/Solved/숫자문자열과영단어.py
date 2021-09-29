# 2021 카카오 채용연계형 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/81301
# 숫자 문자열과 영단어

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# 최적화
def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

# 내가 처음에 푼 방법
def solution(s):
    answer, i = 0, 0
    length = len(s)
    while (i < length):
        if s[i] == "z":
            answer = answer * 10
            i = i + 4
        elif s[i] == "o":
            answer = answer * 10 + 1
            i = i + 3
        elif s[i] == "t":
            if s[i + 1] == "w":
                answer = answer * 10 + 2
                i = i + 3
            else:
                answer = answer * 10 + 3
                i = i + 5
        elif s[i] == 'f':
            if s[i + 1] == "o":
                answer = answer * 10 + 4
                i = i + 4
            else:
                answer = answer * 10 + 5
                i = i + 4
        elif s[i] == "s":
            if s[i + 1] == "i":
                answer = answer * 10 + 6
                i = i + 3
            else:
                answer = answer * 10 + 7
                i = i + 5
        elif s[i] == "e":
            answer = answer * 10 + 8
            i = i + 5
        elif s[i] == "n":
            answer = answer * 10 + 9
            i = i + 4
        else:
            answer = answer * 10 + int(s[i])
            i = i + 1
    return answer