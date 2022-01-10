// 20055 - 컨베이어 벨트 위의 로봇

#include <iostream>
#include <deque>

using namespace std;

// deque 사용?
deque<int> q;
deque<bool> robot;

int main() {

    int N, K, temp;
    cin >> N >> K;

    for (int i = 0; i < 2 * N; i++) {
        cin >> temp;
        q.push_back(temp);
        robot.push_back(false);
    }
    int answer = 1;
    while (1) {
        // 1. Rotate belt
        q.push_front(q.back());
        q.pop_back();

        robot.push_front(robot.back());
        robot.pop_back();
        robot[N - 1] = false;
        // 2. Move Robot
        for (int i = N - 2; i >= 0; i--) {
            if (robot[i] && (!robot[i + 1] && q[i + 1] >= 1)) {
                robot[i + 1] = true;
                robot[i] = false;
                q[i + 1]--;
            }
        }
        robot[N - 1] = false;

        // 3. Insert Robot
        if (q[0] > 0 && !robot[0]) {
            robot[0] = true;
            q[0]--;
        }

        // 4. Check belt
        int check = 0;
        for (int i = 0; i < 2 * N; i++) {
            if (q[i] == 0)
                check++;
        }
        if (check >= K)
            break;

        answer++;
    }
    cout << answer;
    return 0;
}