// 20040 - 사이클 게임
// Disjoint Set 활용하기

#include <iostream>
#include <vector>

using namespace std;

int main() {

    int n, m;
    cin >> n >> m;
    
    // 2차원 벡터 초기화
    vector<vector<int>> graph(n + 1, vector<int>(n + 1, 0));

    for (int i = 0; i < m; i++) {
        int a, b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }



    return 0;
}