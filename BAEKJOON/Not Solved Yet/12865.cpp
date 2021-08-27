// 12865 - 평범한 배낭(배낭 문제)
// 다이나믹 프로그래밍, Knapsack Algorithm

#include <iostream>
#include <vector>

using namespace std;

int main() {

    int total_num, max_weight;

    cin >> total_num >> max_weight;
    
    vector<int> weight;
    vector<int> value;
    vector<int> value_per_weight;

    for (int i = 0; i < total_num; i++) {
        weight.push_back(cin.get());
        value.push_back(cin.get());
        value_per_weight.push_back(value[i] / weight[i]);
    }

    // 무게당 가치를 기준으로 세 배열을 한꺼번에 정리해야함
    // 동적 계획법 사용하기
}