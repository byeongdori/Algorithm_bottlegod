// 1929 - 소수 구하기
// 에라토스테네스의 체 사용
// cout << endl 보다 cout << "\n"이 훨씬 빠르다..

#include <iostream>
#include <cmath>
using namespace std;

int main() {

    int x, y;
    bool* check_arr;
    cin >> x;
    cin >> y;

    // 동적 할당
    check_arr = new bool[y + 1];
    fill_n(check_arr, y + 1, 1);

    check_arr[0] = false;
    check_arr[1] = false;

    // 제곱근 까지만 소수 판별

    for (int i = 2; i <= sqrt(y); i++)
        if (check_arr[i] == true)
            for (int j = i * 2; j <= y; j += i)
                check_arr[j] = false;

    for (int i = x; i <= y; i++)
        if (check_arr[i] == true)
            cout << i << "\n";

    return 0;
}