// 7579 - 앱
// 다이나믹 프로그래밍, 배낭문제

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m, temp;
    int total_cost = 0;
    int answer = 0;
    cin >> n >> m;

    vector<int> memory;
    vector<int> cost;
    memory.push_back(0);
    cost.push_back(0);

    for (int i = 0; i < n; i++) {
        cin >> temp;
        memory.push_back(temp);
    }
   

    for (int i = 0; i < n; i++) {
        cin >> temp;
        cost.push_back(temp);
        total_cost += temp;
    }

    // dp[i] -> i cost의 비용으로 넣을 수 있는 memory의 최댓값
    int* dp = new int[total_cost + 1]{ 0 };

    for (int i = 1; i <= n; i++) {
        for (int j = total_cost; j >= cost[i]; j--) {
            dp[j] = max(dp[j], dp[j - cost[i]] + memory[i]);
        }
    }

    for (int i = total_cost; i >= 0; i--) {
        if (dp[i] >= m)
            answer = i;
    }

    cout << answer;
    delete[] dp;

    return 0;
}