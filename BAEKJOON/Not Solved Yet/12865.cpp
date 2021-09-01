// 12865 - 평범한 배낭(배낭 문제)
// 다이나믹 프로그래밍, Knapsack Algorithm

#include <iostream>
#include <vector>

using namespace std;

int dp[101][100001] = { 0 };

int main() {

    int total_num, max_weight, push_weight, temp;
    cin >> total_num >> max_weight;

    vector<int> weight;
    vector<int> value;
    weight.push_back(0);
    value.push_back(0);

    for (int i = 0; i < total_num; i++) {
        cin >> temp;
        weight.push_back(temp);
        cin >> temp;
        value.push_back(temp);
    }

    for (int i = weight[1]; i <= max_weight; i++) {
        dp[1][i] = value[1];
        cout << "i " << 1 << " j " << i << " dp " << dp[1][i] << endl;
    }

    // 다이나믹 프로그래밍
    // dp[i][j] = max(dp[i-1][j], dp[i][j - 넣을 무게] + 넣을 물품의 가치)
    for (int i = 2; i <= total_num; i++) {
        for (int j = 1; j <= max_weight; j++) {
            push_weight = weight[i];
            if (push_weight - j >= 0)
                dp[i][j] = (dp[i - 1][j] > dp[i][j - push_weight] + value[i])? dp[i - 1][j] : dp[i][j - push_weight] + value[i];
            cout << "i " << i << " j " << j << " dp " << dp[i][j] << endl;
        }
    }

    cout << dp[total_num][max_weight];
}   