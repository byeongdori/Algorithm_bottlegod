// 2164 - 카드2

#include <iostream>
#include <queue>

using namespace std;

int main() {

    int N;
    cin >> N;

    queue<int> q;
    for (int i = 1; i <= N; i++) {
        q.push(i);
    }

    if (q.size() == 1) {
        cout << q.front();
        return 0;
    }

    int temp;
    while(1) {
        q.pop();
        temp = q.front();
        if (q.size() == 1) {
            cout << temp;
            return 0;
        }
        q.pop();
        q.push(temp);
    }
}