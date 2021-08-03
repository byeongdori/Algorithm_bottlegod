// 15552 - 빠른 A + B
/* 빠른 입출력 위해서는 
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL); 필요, 그리고 개행문자 쓰기 (endl X)
*/

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int num;
    cin >> num;

    int input_1, input_2;

    for (int i = 0; i < num; i++)
    {
        cin >> input_1 >> input_2;
        cout << input_1 + input_2 << "\n";
    }
}