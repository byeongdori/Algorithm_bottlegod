// 1927 - 최소 힙

#include <iostream>
#include <stdio.h>
#include <queue>
using namespace std;

int main() {
    int count, temp;
    cin >> count;

    priority_queue<int, vector<int>, greater<int>> min_heap;
    for (int i = 0; i < count; i++) {
        scanf("%d", &temp);
        if (temp == 0) {
            if (min_heap.empty())
                cout << 0;
            else {
                cout << min_heap.top();
                min_heap.pop();
            }
            cout << "\n";
        }
        else {
            min_heap.push(temp);
        }
    }
}