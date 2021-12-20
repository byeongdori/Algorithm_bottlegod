// 1931 - 회의실 배정
// 그리디 알고리즘, 정렬 후, 최선의 선택

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 사용자 정의 정렬 함수!
bool sort_vector(pair<int, int> p1, pair<int, int> p2) {

    if (p1.second == p2.second) {
        return p1.first < p2.first;
    }
    return p1.second < p2.second;
}

int main() {

    int N, a, b;
    cin >> N;

    vector<pair<int, int>> v;

    for (int i = 0; i < N; i++) {
        cin >> a >> b;
        v.emplace_back(pair<int, int> (a, b));
    }
    sort(v.begin(), v.end(), sort_vector);

    int current = 0;
    int answer = 0;
    for (int i = 0; i < N; i++) {
        if (v[i].first >= current) {
            answer++;
            current = v[i].second;
        }
    }

    cout << answer;
    return 0;
}