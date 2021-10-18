// 2017 카카오코드 예선
// https://programmers.co.kr/learn/courses/30/lessons/1829

#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };
bool visit[101][101];

int bfs(int i, int j, int m, int n, vector<vector<int>> picture) {
    int area_size = 1;
    int color = picture[i][j];
    visit[i][j] = true;
    
    queue<pair<int, int>> q;
    q.push(make_pair(i, j));
 
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                if (!visit[nx][ny] && picture[nx][ny] == color) {
                    visit[nx][ny] = true;
                    q.push(make_pair(nx, ny));
                    area_size++;
                }
            }
        }
    }
    return area_size;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {

    int number_of_area = 0;
    int max_size_of_one_area = 0;
 
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            visit[i][j] = false;

    int size_of_one_area;

    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            if (picture[i][j] != 0 && !visit[i][j]) {
                size_of_one_area = bfs(i, j, m, n, picture);
                max_size_of_one_area = max(max_size_of_one_area, size_of_one_area);
                number_of_area++;
            }
        }

    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}
