// 수식 최대화
// 2020 카카오 인턴십
// https://programmers.co.kr/learn/courses/30/lessons/67257?language=cpp

#include <string>
#include <vector>

using namespace std;

vector<int> num;
vector<char> op;

long long solution(string expression) {
    long long answer = 0;

    int len = expression.length();

    int temp = 0;
    for (int i = 0; i < len; i++) {
        if (expression[i] == '+' || expression[i] == '-' || expression[i] == '*') {
            op.push_back(expression[i]);
            num.push_back(temp);
            temp = 0;
        }
        else {
            temp *= 10;
            temp += expression[i];
        }
    }


    return answer;
}

int calculate_op(char first, char second, char third) {
    // for 문 중간에 값 바꿀수 있나?
    return 0;
}