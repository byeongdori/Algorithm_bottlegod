// 12865 - 평범한 배낭(배낭 문제)
// 다이나믹 프로그래밍, Knapsack Algorithm

#include <iostream>
#include <vector>

using namespace std;

int dp[101][100001] = { 0 };

int main() {

    int total_num, max_weight, temp;
    cin >> total_num >> max_weight;

    vector<int> weight;
    vector<int> value;

    for (int i = 0; i < total_num; i++) {
        cin >> temp;
        weight.push_back(temp);
        cin >> temp;
        value.push_back(temp);
    }

    for (int i = weight[0]; i <= max_weight; i++)
        dp[1][i] = value[0];

    // 다이나믹 프로그래밍
    // dp[i][j] = max(dp[i-1][j], dp[i][j - 넣을 무게] + 넣을 물품의 가치)
    for (int i = 1; i <= total_num; i++) {
        for (int j = 1; j <= max_weight; j++) {
            
        }
    }

}