// 20055 - 컨베이어 벨트 위의 로봇

#include <iostream>

using namespace std;

// Queue 사용?
int dura[203] = {0};

int main() {

    int N, K;
    cin >> N >> K;

    for (int i = 1; i <= 2 * N; i++) {
        cin >> dura[i];
        cout << dura[i];
    }

    return 0;
}