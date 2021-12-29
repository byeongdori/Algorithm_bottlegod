// 15681 - 트리와 쿼리
// DFS

#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

int parent[100001];
vector<vector<int>> graph;
vector<int> answer;

int dfs(int parent, int current);

int main() {

    int N, R, Q, U, V;
    cin >> N >> R >> Q;

    graph.resize(N + 1);
    answer.resize(N + 1);
    for (int i = 1; i < N; i++) {
        scanf("%d %d", &U, &V);
        //cin >> U >> V;
        graph[U].push_back(V);
        graph[V].push_back(U);
    }

    dfs(0, R);

    for (int i = 0; i < Q; i++) {
        int temp;
        scanf("%d", &temp);
        //cin >> temp;
        cout << answer[temp] << "\n";
    }
    return 0;
}

int dfs(int parent, int current) {
    
    int result = 0;

    for (int next : graph[current]) {
        if (parent == next)
            continue;

        result += dfs(current, next);
    }

    return answer[current] = result + 1;
}