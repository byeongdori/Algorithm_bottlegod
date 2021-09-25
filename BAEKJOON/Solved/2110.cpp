// 2110 - 공유기 설치
// 이분 탐색, 매개변수 탐색

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    int n, c, temp;
    vector<int> position;

    cin >> n >> c;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        position.push_back(temp);
    }

    sort(position.begin(), position.end());

    int start = 1;
    int end = position[n - 1] - position[0];
    int result = 0;

    while (start <= end) {
        int middle = (start + end) / 2;
        int count = 1;
        int prev_position = position[0];
        
        for (int i = 1; i < n; i++) {
            if (position[i] - prev_position >= middle) {
                count++;
                prev_position = position[i];
            }
        }

        if (count < c)
            end = middle - 1;
        else {
            result = max(middle, result);
            start = middle + 1;
        }
    }

    cout << result;
    return 0;
}