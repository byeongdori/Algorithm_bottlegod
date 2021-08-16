// 15651 - N과 M (3)
// 1~N개까지의 자연수 중에서 M개 선택하여 출력 / 중복허용
// 백트래킹
// 빠른 입출력("\n") 사용

#include <iostream>
#include <vector>

using namespace std;

void back_tracking(int n, int m, int loop);

vector<int> arr;

int main() {
    int n, m;

    cin >> n;
    cin >> m;

    back_tracking(n, m, 0);
}

void back_tracking(int n, int m, int loop) {

    // 재귀 종료 조건
    if (loop == m) {
        vector<int>::iterator it;
        for (it = arr.begin(); it < arr.end(); it++)
            cout << *it << " ";
        cout << "\n";
        return;
    }

    // 재귀 내부
    for (int i = 0; i < n; i++) {
        arr.push_back(i+1);
        back_tracking(n, m, loop + 1);
        arr.pop_back();
    }
}