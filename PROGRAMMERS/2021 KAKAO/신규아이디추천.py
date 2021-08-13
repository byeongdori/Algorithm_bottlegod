# 2021 KAKAO BULID RECRUITMENT
# 7단계 과정 통해 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

def solution(new_id):

    # 1단계 - 모든 알파벳 소문자로 변환
    answer = new_id.lower()

    # 2단계 - 허용하지 않는 특수문자 제거
    delete_char = "~!@#$%^&*()=+[{]}:?,<>/"
    for i in range(len(delete_char)):
        answer = answer.replace(delete_char[i], "")
    
    # 3단계 - 연속된 마침표 제거
    temp = answer
    answer = []
    for i in range(len(temp)):
        if temp[i] == "." and temp[i-1] == "." and i != 0:
            continue
        else:
            answer.append(temp[i])

    # 4단계 - 맨 앞, 뒤 마침표 제거
    if len(answer) >= 1:
        if answer[0] == ".":
            answer.pop(0)
        if len(answer) != 0 and answer[len(answer) - 1] == ".":
            answer.pop(len(answer) - 1)

        
    # 5단계 - 결과가 빈 문자열이면, "a" 추가
    if len(answer) == 0:
        answer.append("a")
    print(answer)

    # 6단계 - 결과가 16자 이상인 경우, 최대 15자로 잘라내기
    # 이때, 잘라낸 후 결과의 마지막 문자가 마침표인 경우 마침표 제거
    if len(answer) >= 16:
        del answer[15:]
        if answer[14] == ".":
            del answer[14]
    print(answer)

    # 7단계 - 결과가 2자 이하인 경우, 길이가 3이 될때까지 마지막 문자 반복
    if len(answer) <= 2:
        while len(answer) < 3:
            answer.append(answer[len(answer) - 1])

    # 최종
    answer = "".join(answer)
    return answer
