// 11403 - 경로 찾기
// 플로이드-와셜 알고리즘

#include <iostream>

using namespace std;

int graph[101][101] = { 0 };

int main() {

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> graph[i][j];
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                if (graph[j][i] >= 1 && graph[i][k] >= 1)
                    graph[j][k] = 1;
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
                cout << graph[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}