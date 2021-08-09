// 18870 - 좌표 압축
// 벡터 사용해서 다시 풀기 -> 중복 제거, 정렬, 출력

#include <iostream>

using namespace std;

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int count_of_num;
	cin >> count_of_num;

	int* arr = new int[count_of_num];
	int* resultarr = new int[count_of_num];

	for (int i = 0; i < count_of_num; i++) {
		resultarr[i] = 0;
		cin >> arr[i];
	}

	for (int i = 0; i < count_of_num; i++) {
		for (int j = 0; i < count_of_num; j++) {
			if (arr[i] < arr[j])
				resultarr[j] = resultarr[j] + 1;
		}
	}

	for (int i = 0; i < count_of_num; i++)
		cout << resultarr[i];

	delete[] arr;
	delete[] resultarr;
}