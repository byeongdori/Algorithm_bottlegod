// 5639 - 이진 검색 트리
// 재귀적으로 호출

#include <iostream>
#include <vector>

using namespace std;

vector<int> tree;
void postorder(int left, int right);

int main() {

    int temp;
    while (cin >> temp) {
        if (temp == EOF)
            break;
        tree.push_back(temp);
    }

    postorder(0, tree.size() - 1);
    return 0;
}

void postorder(int left, int right) {

    int i = left + 1;
    int temp = tree[left];

    while (i < tree.size() && temp > tree[i])
        i++;

    if (i - 1 > left)
        postorder(left + 1, i - 1);
    if (i <= right)
        postorder(i, right);
    cout << tree[left] << "\n";
}