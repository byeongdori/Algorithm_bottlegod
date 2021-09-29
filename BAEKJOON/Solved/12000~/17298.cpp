// 17298 - 오큰수
// 스택과 배열의 인덱스 활용

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    int size, temp;
    stack<int> index_stack;

    cin >> size;
    vector<int> input_num, answer(size);
    for (int i = 0; i < size; i++) {
        cin >> temp;
        input_num.push_back(temp);
        
    }

    // 인덱스를 스택에 집어넣음, 오큰수를 만나면 스택에 있는 인덱스를 빼내어 결과 배열에 저장
    index_stack.push(0);
    for (int i = 1; i < size; i++) {
        while (!index_stack.empty() && input_num[index_stack.top()] < input_num[i] ) {
            answer[index_stack.top()] = input_num[i];
            index_stack.pop();
        }
        index_stack.push(i);
    }

    while (!index_stack.empty()) {
        answer[index_stack.top()] = -1;
        index_stack.pop();
    }

    vector<int>::iterator it;
    for (it = answer.begin(); it < answer.end(); it++)
        cout << *it << " ";
}