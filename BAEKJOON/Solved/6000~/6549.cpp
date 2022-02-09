// 6549 - 히스토그램에서 가장 큰 직사각형

#include <iostream>
#include <algorithm>

using namespace std;

long long num;
long long seg_tree[400001];
long long histogram[100001];

long long make_seg_tree(int node, int start, int end);
long long find_seg_tree(int node, int start, int end, int left, int right);
long long find_size(long long left, long long right);

int main() {

    cin.tie(0)->sync_with_stdio(0);
    cout.tie(0);

    histogram[0] = 1e10;
    while (1) {

        // 값 넣는 과정
        cin >> num;
        if (num == 0)
            return 0;

        for (int i = 1; i <= num; i++)
            cin >> histogram[i];

        make_seg_tree(1, 1, num);
        cout << find_size(1, num) << "\n";
    }
    return 0;
}

long long make_seg_tree(int node, int start, int end) {

    if (start == end) {
        seg_tree[node] = start;
        return seg_tree[node];
    }

    int mid = (start + end) / 2;
    long long a = make_seg_tree(node * 2, start, mid);
    long long b = make_seg_tree(node * 2 + 1, mid + 1, end);

    if (histogram[a] > histogram[b])
        seg_tree[node] = b;
    else
        seg_tree[node] = a;

    return seg_tree[node];
}

long long find_seg_tree(int node, int start, int end, int left, int right) {

    if (start > right || end < left)
        return 0;

    if (start >= left && end <= right)
        return seg_tree[node];

    int mid = (start + end) / 2;
    long long a = find_seg_tree(node * 2, start, mid, left, right);
    long long b = find_seg_tree(node * 2 + 1, mid + 1, end, left, right);

    if (histogram[a] > histogram[b])
        return b;
    else
        return a;
}

long long find_size(long long left, long long right) {

    if (left > right)
        return 0;

    int min_index = find_seg_tree(1, 1, num, left, right);
    long long answer = (right - left + 1) * histogram[min_index];
    answer = max(answer, find_size(left, min_index - 1));
    answer = max(answer, find_size(min_index + 1, right));
    return answer;
}