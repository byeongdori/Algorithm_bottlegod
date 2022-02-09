// 1541 - 잃어버린 괄호

#include <iostream>
#include <vector>

using namespace std;

int main() {
    string input;
    cin >> input;

    int temp = 0;
    vector<int> num;
    vector<char> op;
    // 입력 받기
    for (int i = 0; i < input.length(); i++) {
        if (input[i] == '+' || input[i] == '-') {
            num.push_back(temp / 10);
            op.push_back(input[i]);
            temp = 0;
        }
        else {
            temp += input[i] - 48;
            temp *= 10;
            if (i == input.length() - 1) 
                num.push_back(temp / 10);
        }
    }

    
    int answer = num[0];
    bool minusappear = false;
    for (int i = 0; i < op.size(); i++) {
        if (op[i] == '-') {
            minusappear = true;
            answer -= num[i + 1];
        }
        else if (minusappear == true) {
            answer -= num[i + 1];
        }
        else {
            answer += num[i + 1];
        }
    }

    cout << answer;
}