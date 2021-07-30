// 1929 - 소수 구하기
// 에라토스테네스의 체 사용해서 다시 풀기

#include <iostream>
#include <math.h>
using namespace std;

int main() {

    int x, y;
    cin >> x >> y;

    bool check_arr[1000001];

    for (int i = 1; i < 1000001; i++)
        check_arr[i] = true;

    check_arr[1] = false;

    // 제곱근 까지만 소수 판별

    int root_y = int(sqrt(y));

    for (int i = 2; i <= root_y; i++)
    {
        if (check_arr[i] == true)
        {
            for (int j = 2; i * j <= 1000001; j++)
                check_arr[i * j] = false;
        }
    }

    for (int i = x; i <= y; i++)
    {
        if (check_arr[i] == true)
            cout << i << endl;
    }
}