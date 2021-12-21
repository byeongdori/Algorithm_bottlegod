// 10814 - 나이순 정렬
// Stable sort

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool vector_sort(pair<int, string> p1, pair<int, string> p2) {
    return p1.first < p2.first;
}

int main() {

    int N;
    cin >> N;

    vector<pair<int, string>> v;
    for (int i = 0; i < N; i++) {
        int temp;
        string temp_string;

        cin >> temp >> temp_string;
        v.push_back(make_pair(temp, temp_string));
    }
    stable_sort(v.begin(), v.end(), vector_sort);

    for (int i = 0; i < N; i++) {
        cout << v[i].first << " " << v[i].second;
        if (i != N - 1)
            cout << "\n";
    }
}