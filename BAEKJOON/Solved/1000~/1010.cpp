// 1010 - 다리 놓기
// 단순 이항계수 구하는 문제
// 다이나믹 프로그래밍 (11051번 문제 코드 활용)

#include <iostream>

using namespace std;

int combi[30][30] = { 0 };

int main() {
    int test_case, n, m;
    cin >> test_case;

    while (test_case > 0) {
        cin >> n >> m;
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < i + 1; j++) {
                if (j == 1)
                    combi[i][j] = i;
                else if (j == i)
                    combi[i][j] = 1;
                else
                    combi[i][j] = combi[i - 1][j - 1] + combi[i - 1][j];
                }
            }
    cout << combi[m][n] << "\n";
    test_case--;
    }
}