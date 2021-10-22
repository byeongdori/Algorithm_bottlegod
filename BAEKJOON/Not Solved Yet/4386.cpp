// 4386 - 별자리 만들기

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int parent[101];
vector<pair<double, double>> star;
vector<tuple<double, int, int>> dist;

int main() {

    int n;
    cin >> n;

    // 부모 초기화
    for (int i = 0; i <= 100; i++)
        parent[i] = i;

    // 별의 좌표 입력
    star.push_back({0, 0});
    for (int i = 1; i <= n; i++) {
        float a, b;
        cin >> a >> b;
        star.push_back({a, b});
    }

    // 별 간의 거리 계산
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            double x_dis = pow(star[i].first - star[j].first, 2);
            double y_dis = pow(star[i].second - star[j].second, 2);
            dist.push_back({x_dis + y_dis, i, j});
        }
    }

    return 0;
}