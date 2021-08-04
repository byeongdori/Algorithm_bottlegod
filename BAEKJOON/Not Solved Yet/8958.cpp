// 8958 - O/X 퀴즈
// 문자열 비교 다시하기!
#include <iostream>
#include <string>

using namespace std;

int main() {

    int total_score, score, test_case;

    cin >> test_case;
    cin.get();

    char inputOX[80];

    for (int i = 0; i < test_case; i++) {
        cin.getline(inputOX, 81);
        total_score = 0;
        score = 1;
        int j = 0;
        while (inputOX[j] == 'O' || inputOX[j] == 'X') {
            if (inputOX[j] == '0') {
                cout << "hello";
                if (j != 0 && inputOX[j - 1] != '0')
                    score = 1;
                total_score += score;
            }
            else
                score = 1;
            j += 1;
        }
        cout << total_score << endl;
    }
}