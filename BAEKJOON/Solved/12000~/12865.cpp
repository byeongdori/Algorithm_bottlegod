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

    // 다이나믹 프로그래밍, 한 물건을 여러번 X
    // i번째 까지의 물건을 j의 무게로 담는 경우
    // dp[i][j] = max(dp[i-1][j], dp[i - 1][j - 넣을 무게] + 넣을 물품의 가치)
    for (int i = 1; i <= total_num; i++) {
        for (int j = 1; j <= max_weight; j++) {
            push_weight = weight[i];
            if (j - push_weight >= 0)
                dp[i][j] = (dp[i - 1][j] > (dp[i - 1][j - push_weight] + value[i])) ? dp[i - 1][j] : dp[i - 1][j - push_weight] + value[i];
            else
                dp[i][j] = dp[i - 1][j];
        }
    }

    cout << dp[total_num][max_weight];
}