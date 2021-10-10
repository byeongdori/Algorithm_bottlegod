// 9252 - LCS 2
// 다이나믹 프로그래밍, 이차원 배열 생성해서 비교

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 최대 1000글자, 이거 전역으로 선언안하면 오류 뜸
int LCS_arr[1001][1001];

int main() {

    string input_1, input_2;
    vector<char> resultLCS;

    getline(cin, input_1);
    getline(cin, input_2);


    // LCS 찾기
    for (int i = 1; i <= input_1.size(); i++)
        for (int j = 1; j <= input_2.size(); j++) {
            if (input_1[i - 1] == input_2[j - 1])
                LCS_arr[i][j] = LCS_arr[i - 1][j - 1] + 1;
            else {
                LCS_arr[i][j] = (LCS_arr[i][j - 1] > LCS_arr[i - 1][j]) ? LCS_arr[i][j - 1] : LCS_arr[i - 1][j];
            }
        }

    // LCS 출력
    int i = input_1.size();
    int j = input_2.size();

    cout << LCS_arr[i][j] << endl;

    if (LCS_arr[i][j] != 0) {
        while (LCS_arr[i][j] != 0) {
            if (LCS_arr[i][j] == LCS_arr[i - 1][j])
                i--;
            else if (LCS_arr[i][j] == LCS_arr[i][j - 1])
                j--;
            else {
                resultLCS.push_back(input_1[i - 1]);
                i--;
                j--;
            }
        }

        reverse(resultLCS.begin(), resultLCS.end());
        for (i = 0; i < resultLCS.size(); i++)
            cout << resultLCS[i];
    }
}