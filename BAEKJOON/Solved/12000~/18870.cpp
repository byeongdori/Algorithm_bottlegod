// 18870 - 좌표 압축
// 벡터 정렬, 중복 제거
// lower_bound 함수 이용하기

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	int count_of_num, temp;
	cin >> count_of_num;

	vector<int> input_vector;
	vector<int> temp_vector;

	for (int i = 0; i < count_of_num; i++) {
		cin >> temp;
		input_vector.push_back(temp);
	}

	temp_vector = input_vector;

	// 벡터 정렬 & 중복 제거
	sort(input_vector.begin(), input_vector.end());
	input_vector.erase(unique(input_vector.begin(), input_vector.end()), input_vector.end());

	// lower_bound 함수 이용해서 위치 찾은다음, 압축된 값 출력 
	for (int it : temp_vector) {
		int result = lower_bound(input_vector.begin(), input_vector.end(), it) - input_vector.begin();
		cout << result << " ";
	}
}