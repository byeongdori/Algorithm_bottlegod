// 10830 - 행렬 제곱

#include <iostream>

using namespace std;

int arr[5][5] = {0};

int main() {
    int n, size;
    cin >> n >> size;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++){
            arr[i][j] = cin.get();
        }
    }
}