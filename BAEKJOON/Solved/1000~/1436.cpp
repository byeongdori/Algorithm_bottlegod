// 1436 - 영화감독 숌
// 666부터 시작하여 모든 경우 탐색 (Brute-Forth)

#include <iostream>

using namespace std;

int main() {

	int input, temp;
	int index = 666;
	int count = 0;
	cin >> input;

	while (1) {
		temp = index;
		while (temp >= 666) {
			if (temp % 1000 == 666) {
				count++;
				break;
			}
			else
				temp /= 10;
		}
		if (count == input)
			break;
		index++;
	}

	cout << index;
}