// 1956 - 운동
// 그래프
// 플로이드-와샬 알고리즘

#include <iostream>
#include <stdio.h>

using namespace std;

int graph[401][401] = {0};

int main() {

    int V, E, a, b, c;
    cin >> V >> E;

    for (int i = 0; i < E; i++) {
        scanf("%d %d %d", &a, &b, &c);
        graph[a][b] = c;
    }

    // 플로이드-와샬 알고리즘
    return 0;
}