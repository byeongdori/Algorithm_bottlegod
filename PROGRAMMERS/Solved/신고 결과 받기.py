# 2022 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/92334
# 신고 결과 받기

from collections import Counter

def solution(id_list, report, k):
    answer = []
    report_dict = {}

    report = set(report)
    check_report = []

    for report_from in id_list:
        report_dict[report_from] = []

    for case in report:
        report_from, report_to = case.split()
        report_dict[report_from].append(report_to)
        check_report.append(report_to)

    count_list = Counter(check_report)

    for i in id_list:
        temp = 0
        for r in report_dict[i]:
            if count_list[r] >= k:
                temp += 1
        answer.append(temp)

    return answer
