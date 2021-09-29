// 1065 - 한수
// input은 1000이하의 자연수

#include <iostream>

using namespace std;

int main() {
    int input, A, B, C;
    int count = 0;

    cin >> input;

    if (input <= 99) {
        cout << input;
        return 0;
    }

    for (int i = 100; i <= input; i++) {
        A = i % 10;
        B = (i / 10) % 10;
        C = (i / 10) / 10;
        if ((B - A) == (C - B))
            count++;
    }
    cout << count + 99;
}