// 17298 - 오큰수

#include <iostream>
#include <stack>

using namespace std;

int main() {
    int size;
    stack<int> num_stack;

    cin >> size;
    for (int i = 0; i < size; i++) {
        int temp;
        cin >> temp;
        num_stack.push(temp);
    }

}