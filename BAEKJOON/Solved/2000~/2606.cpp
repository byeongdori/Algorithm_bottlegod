// 2606 - 바이러스
// BFS

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>
#include <queue>

using namespace std;

int graph[101][101] = { 0 };
bool virus[101] = { false };

int main() {
    int n, m, current;
    int count = 0;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d",&a,&b);
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    queue<int> q;
    q.push(1);
    virus[1] = true;
    while (!q.empty()) {
        current = q.front();
        q.pop();
        for (int i = 1; i <= n; i++) {
            if (graph[current][i] == 1 && !virus[i]) {
                virus[i] = true;
                q.push(i);
                count++;
            }
        }
    }

    cout << count;
    return 0;
}