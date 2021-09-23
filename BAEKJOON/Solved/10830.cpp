// 10830 - 행렬 제곱
// 분할정복
// 큰 수는 long long 사용하기!

#include <iostream>

using namespace std;

int arr_size;
long long n;
int arr[5][5] = { 0 };
int temp[5][5] = { 0 };
int answer[5][5] = { 0 };
void matrix_multiple(int a[][5], int b[][5]);

int main() {

    cin >> arr_size >> n;

    for (int i = 0; i < arr_size; i++) {
        for (int j = 0; j < arr_size; j++)
            cin >> arr[i][j];
        answer[i][i] = 1;
    }

    while (n > 0) {
        if (n % 2 == 1)
            matrix_multiple(answer, arr);
        matrix_multiple(arr, arr);
        n /= 2;
    }

    for (int i = 0; i < arr_size; i++) {
        for (int j = 0; j < arr_size; j++) {
            cout << answer[i][j];
            if (j != arr_size - 1)
                cout << " ";
        }
        if (i != arr_size - 1)
            cout << endl;
    }
}

void matrix_multiple(int a[][5], int b[][5]) {
    for (int i = 0; i < arr_size; i++)
        for (int j = 0; j < arr_size; j++)
        {
            temp[i][j] = 0;
            for (int k = 0; k < arr_size; k++)
                temp[i][j] += (a[i][k] * b[k][j]);

            temp[i][j] %= 1000;
        }

    for (int i = 0; i < arr_size; i++)
        for (int j = 0; j < arr_size; j++)
            a[i][j] = temp[i][j];
}