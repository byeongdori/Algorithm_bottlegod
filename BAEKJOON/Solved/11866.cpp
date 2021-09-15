// 11866 - 요세푸스 문제 0
// Queue 사용

#include <iostream>
#include <queue>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    queue<int> temp;

    for (int i = 1; i < n + 1; i++)
        temp.push(i);

    cout << "<";
    for (int i = 1; i < n + 1; i++) {
        for (int j = 0; j < k - 1; j++) {
            temp.push(temp.front());
            temp.pop();
        }
        if (i != n)
            cout << temp.front() << ", ";
        else
            cout << temp.front();
        temp.pop();
    }
    cout << ">";
}