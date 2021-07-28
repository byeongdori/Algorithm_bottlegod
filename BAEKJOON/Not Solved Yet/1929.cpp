// 1929 - 소수 구하기
// 에라토스테네스 체 사용해서 다시 풀기
#include <iostream>
#include <math.h>
using namespace std;

int main() {

    int x, y;
    int sqrt_x;
    cin >> x >> y;

    // 제곱근 까지만 소수 판별

    for (x; x <= y; x++)
    {
        if (x == 1)
            continue;

        if (x == 2 || x == 3)
        {
            cout << x << endl;
            continue;
        }

        if (x % 2 == 0 || x % 3 == 0)
            continue;

        sqrt_x = int(sqrt(x));
        for (int z = 2; z <= sqrt_x; z++)
        {
            cout << "double roop" << x << endl;

            if (x % z == 0 && z != 1) 
                break;
            if (z == sqrt_x)
                cout << x << endl;
        }
    }
}