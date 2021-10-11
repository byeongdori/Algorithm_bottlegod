// 1991 - 트리 순회

#include <iostream>

using namespace std;

typedef struct Node {
    char data;
    Node* left;
    Node* right;
} Node;

void preorder(Node *node);
void inorder(Node *node);
void postorder(Node *node);

int main() {

    int n;
    Node* nodes;
    cin >> n;

    nodes = (Node*)malloc(sizeof(Node) * n);

    for (int i = 0; i < n; i++) {
        char a, b, c;
        cin >> a >> b >> c;

        nodes[a - 'A'].data = a;

        if (b == '.')
            nodes[a - 'A'].left = NULL;
        else
            nodes[a - 'A'].left = &nodes[b - 'A'];

        if (c == '.')
            nodes[a - 'A'].right = NULL;
        else
            nodes[a - 'A'].right = &nodes[c - 'A'];
    }

    // 전위
    preorder(&nodes[0]);
    cout << endl;
    // 중위
    inorder(&nodes[0]);
    cout << endl;
    // 후위
    postorder(&nodes[0]);

    free(nodes);
    return 0;
}

void preorder(Node* node) {

    if (node == NULL)
        return;

    cout << node->data;
    preorder(node->left);
    preorder(node->right);
}

void inorder(Node* node) {

    if (node == NULL)
        return;

    inorder(node->left);
    cout << node->data;
    inorder(node->right);
}

void postorder(Node* node) {

    if (node == NULL)
        return;

    postorder(node->left);
    postorder(node->right);
    cout << node->data;
}