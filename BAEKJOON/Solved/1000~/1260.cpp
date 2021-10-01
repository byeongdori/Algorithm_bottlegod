// 1260 - DFS와 BFS

#include <iostream>
#include <queue>

using namespace std;

int graph[1001][1001] = {0};
bool visit[1001] = {false};
int N, M, V, a, b;
queue<int> result;

void dfs(int v);
void bfs(int v);

int main() {
    
    cin >> N >> M >> V;
    for (int i = 0; i < M; i++) {
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }
    dfs(V);
    
    for (int i = 0; i < 1001; i++)
        visit[i] = false;

    cout << endl;
    bfs(V);

    return 0;
}

void dfs(int v) {
    visit[v] = true;
    cout << v << " ";

    for (int i = 1; i <= N; i++) {
        if (graph[v][i] == 1 && visit[i] == false)
            dfs(i);
    }
};

void bfs(int v) {
    result.push(v);
    visit[v] = true;
    cout << v << " ";

    while (!result.empty()) {
        v = result.front();
        result.pop();

        for (int i = 1; i <= N; i++) {
            if (graph[v][i] == 1 && visit[i] == false) {
                result.push(i);
                visit[i] = true;
                cout << i << " ";
            }
        }
    }
};