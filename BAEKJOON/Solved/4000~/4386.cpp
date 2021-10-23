// 4386 - 별자리 만들기
// 크루스칼 알고리즘, Disjoint set

#include <iostream>
#include <stdio.h>
#include <vector>
#include <cmath>
#include <algorithm>
#include <tuple>

using namespace std;

int parent[101];
vector<pair<double, double>> star;
vector<tuple<double, int, int>> dist;
double answer;

int find_parent(int i) {
    if (parent[i] == i)
        return i;
    else
        return find_parent(parent[i]);
}

int main() {

    int n;
    cin >> n;

    // 부모 초기화
    for (int i = 1; i <= 100; i++)
        parent[i] = i;

    // 별의 좌표 입력
    star.push_back({ 0, 0 });
    for (int i = 1; i <= n; i++) {
        double a, b;
        cin >> a >> b;
        star.push_back({ a, b });
    }

    // 별 간의 거리 계산
    for (int i = 1; i <= n - 1; i++) {
        for (int j = i + 1; j <= n; j++) {
            double x_dis = pow(star[i].first - star[j].first, 2);
            double y_dis = pow(star[i].second - star[j].second, 2);
            dist.push_back({sqrt(x_dis + y_dis), i, j});
        }
    }

    // 별 간 거리 정렬
    sort(dist.begin(), dist.end());

    // 크루스칼 알고리즘 적용하기
    for (int i = 0; i < dist.size(); i++) {
        int a = get<1>(dist[i]);
        int b = get<2>(dist[i]);
        double dis = get<0>(dist[i]);

        a = find_parent(a);
        b = find_parent(b);

        if (a != b) {
            parent[a] = b;
            answer += dis;
        }
    }

    printf("%.2f", answer);
    return 0;
}