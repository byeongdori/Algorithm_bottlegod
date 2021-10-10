// 2017 카카오코드 예선
// https://programmers.co.kr/learn/courses/30/lessons/1829

#include <vector>
#include <queue>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {

    int number_of_area = 0;
    int max_size_of_one_area = 0;

    int color;
    bool visit[101][101] = {false};
    queue<pair<int, int>> q;
    
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++) {
            if (picture[i][j] != 0 & visit[i][j] == false)
                // bfs 실행
                ;
        }









    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}