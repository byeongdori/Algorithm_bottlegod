// 15681 - 트리와 쿼리

#include <iostream>

using namespace std;

int parent[100001];

int main() {

    int N, R, Q, U, V;
    cin >> N >> R >> Q;

    for (int i = 1; i<= N; i++)
        parent[i] = i;

    for (int i = 1; i < N; i++) {
        cin >> U >> V;
        parent[U] = V;
    }

    for (int i = 0; i < Q; i++) {
        cin >> Q;
        int answer = 0;
        
    }
    return 0;
}