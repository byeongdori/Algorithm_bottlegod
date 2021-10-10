// 1644 - 소수의 연속합
// 에라토스테네스의 체 + 투 포인터

#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main() {

    int n, result, sum;
    int left = 0;
    int right = 0;
    vector<int> pn;

    cin >> n;
    if (n == 1 || n == 2) {
        cout << n - 1;
        return 0;
    }

    vector<bool> check(n + 1, true);

    for (int i = 2; i <= n; i++) {
        if (check[i] == true) {
            pn.push_back(i);
            for (int j = i + i; j <= n; j += i)
                check[j] = false;
        }
    }

    result = 0;
    sum = 0;
    while (1) {
        if (sum >= n)
            sum -= pn[left++];
        else if (right == pn.size())
            break;
        else
            sum += pn[right++];
        
        if (sum == n)
            result++;
    }
 
    cout << result;

    return 0;
}