// 11725 - 트리의 부모 찾기
// 벡터와 bfs 이용해서 다시 풀기!

#include <iostream>
#include <stdio.h>

using namespace std;

typedef struct Node {
    int data;
    Node* parent;
} Node;

int main() {

    Node* nodes;
    int n;

    cin >> n;
    nodes = (Node*)malloc(sizeof(Node) * (n + 1));

    for (int i = 1; i <= n; i++) {
        nodes[i].parent = NULL;
        nodes[i].data = i;
    }

    for (int i = 0; i < n - 1; i++) {
        int a, b;
        scanf_s("%d %d", &a, &b);
        if (a == 1)
            nodes[b].parent = &nodes[a];
        else if (b == 1)
            nodes[a].parent = &nodes[b];
        else {
            if (nodes[a].parent == NULL)
                nodes[a].parent = &nodes[b];
            else
                nodes[b].parent = &nodes[a];
        }
    }  

    for (int i = 2; i <= n; i++) {
        if (nodes[i].parent != NULL)
            printf("%d\n", nodes[i].parent->data);
    }

    free(nodes);
    return 0;
}