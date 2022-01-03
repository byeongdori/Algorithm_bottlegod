// 20057 - 마법사 상어와 토네이도

#include <iostream>

using namespace std;

int arr[500][500] = { 0 };
// 0 - 서쪽, 1 - 남쪽, 2 - 동쪽, 3 - 북쪽
int dy[4] = { 0, 1, 0, -1 };
int dx[4] = { -1, 0, 1, 0 };
int answer = 0;

int spread_dy[4][10] =
{
    {-1, 1, -2, 2, -1, 1, -1, 1, 0, 0},
    {-1, -1, 0, 0, 0, 0, 1, 1, 2, 1},
    {-1, 1, -2, 2, -1, 1, -1, 1, 0, 0},
    {1, 1, 0, 0, 0, 0, -1, -1, -2, -1}
};
int spread_dx[4][10] =
{
    {1, 1, 0, 0, 0, 0, -1, -1, -2, -1},
    {-1, 1, -2, 2, -1, 1, -1, 1, 0, 0},
    {-1, -1, 0, 0, 0, 0, 1, 1, 2, 1},
    {-1, 1, -2, 2, -1, 1, -1, 1, 0, 0}
};
int percentage[9] = { 1, 1, 2, 2, 7, 7, 10, 10, 5 };
int N;

void tornado(int y, int x, int direction);

int main() {

    cin >> N;

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> arr[i][j];
        }
    }
    int start_y = (N + 1) / 2;
    int start_x = (N + 1) / 2;
    int step = 1;
    int step_temp = 0;
    int dir = 0;

    while (step <= N) {

        bool exit = false;
        for (int i = 1; i <= 2; i++) {
            for (int j = 0; j < step; j++) {
                tornado(start_y, start_x, dir);
                start_y += dy[dir];
                start_x += dx[dir];
            }
            dir = (dir + 1) % 4;
            if (i == 2 && step == N) {
                exit = true;
                break;
            }
        }
        if (exit == true)
            break;
        step++;
    }

    cout << answer;
    return 0;
}

void tornado(int y, int x, int direction) {
    int current_sand = arr[y + dy[direction]][x + dx[direction]];
    int temp = current_sand;
    for (int i = 0; i < 9; i++) {
        int ny = y + dy[direction] + spread_dy[direction][i];
        int nx = x + dx[direction] + spread_dx[direction][i];
        if (ny > N || ny < 1 || nx > N || nx < 1) {
            answer += (int)(current_sand * percentage[i] / 100);
        }
        else {
            arr[ny][nx] += (int)(current_sand * percentage[i] / 100);
        }
        temp -= (int)(current_sand * percentage[i] / 100);
    }

    int ny = y + dy[direction] + spread_dy[direction][9];
    int nx = x + dx[direction] + spread_dx[direction][9];
    if (ny > N || ny < 1 || nx > N || nx < 1) {
        answer += temp;
    }
    else {
        arr[ny][nx] += temp;
    }

    arr[y + dy[direction]][x + dx[direction]] = 0;
}