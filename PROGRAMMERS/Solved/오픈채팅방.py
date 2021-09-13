# 2019 KAKAO BULID RECRUITMENT
# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888
# dict 자료형 사용!

def solution(record):
    answer = []
    chat_log = []
    user_log = dict()

    for i in range(len(record)):
        record_split = record[i].split()
        if record_split[0] == "Enter":
            chat_log.append([record_split[1], "님이 들어왔습니다."])
            user_log[record_split[1]] = record_split[2]
        elif record_split[0] == "Change":
            user_log[record_split[1]] = record_split[2]
        elif record_split[0] == "Leave":
            chat_log.append([record_split[1], "님이 나갔습니다."])
    
    for chat in chat_log:
        answer.append(user_log[chat[0]] + chat[1])
    return answer
