// 20040 - 사이클 게임
// Disjoint Set 활용하기

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int parent[500001] = {0};

// 부모 찾는 함수
int find(int index)
{
    if (parent[index] == index)
        return index;
    else
        return parent[index] = find(parent[index]);
}

int main() {

    int n, m;
    scanf("%d %d", &n, &m);
    // cin >> n >> m;
    
    for (int i = 1; i <= n; i++)
        parent[i] = i;

    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        // cin >> a >> b;
        a = find(a);
        b = find(b);

        if (a == b) {
            cout << i + 1;
            return 0;
        }
        else
            parent[a] = b;
    }

    cout << 0;
    return 0;
}