// 6549 - 히스토그램에서 가장 큰 직사각형
// 이거 종만북에 있었던 것 같은데 참고하기ㅎ
// https://nnnlog.tistory.com/15
#include <iostream>
#include <vector>

using namespace std;

int seg_tree[100001];
vector<int> histogram;

int find_min_index(int left, int right);

int main() {

    while (1) {

        // 값 넣는 과정
        int min_index;
        long long num;
        long long min_height = 1000000000;
        cin >> num;
        if (num == 0)
            return 0;
        for (int i = 0; i < num; i++) {
            int temp;
            cin >> temp;
            histogram.push_back(temp);
        }
        

        // 구간에서 최소 찾기
        for (int i = 0; i< histogram.size(); i++) {
            if (min_height > histogram[i]) {
                min_height = histogram[i];
                min_index = min_height;
            }
        }
    }

    vector<int> a; 
    int test_case;
    return 0;
}

// 최소 높이 가진 블록 재귀적으로 찾기
int find_min_index(int left, int right) {
    
    if (left == right)
        return left;
    
    
    int mid = (left + right) / 2;

}