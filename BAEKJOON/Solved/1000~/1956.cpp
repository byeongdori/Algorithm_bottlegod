// 1956 - 운동
// 그래프
// 플로이드-와샬 알고리즘

#include <iostream>
#include <stdio.h>
#include <algorithm>

#define INT_MAX 10000000
using namespace std;

int graph[401][401];

int main() {
    int V, E, a, b, c;
    int result = INT_MAX;
    cin >> V >> E;

    // fill 함수로 2차원 배열 초기화!
    fill(graph[0], graph[401], INT_MAX);

    for (int i = 0; i < E; i++) {
        scanf("%d %d %d", &a, &b, &c);
        graph[a][b] = c;
    }

    // 플로이드-와샬 알고리즘
    for (int k = 1; k <= V; k++)         // 거쳐가는 노드
        for (int i = 1; i <=V; i++)      // 시작 노드
            for (int j = 1; j<=V; j++) { // 도착 노드
                if (graph[i][j] > graph[i][k] + graph[k][j])
                    graph[i][j] = graph[i][k] + graph[k][j];
            }

    for (int i = 1; i <=V; i++)
        result = min(result, graph[i][i]);
    
    if (result == INT_MAX)
        cout << - 1;
    else
        cout << result; 

    return 0;
}