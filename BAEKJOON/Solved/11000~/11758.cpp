// 11758 - CCW
// Counter Clock Wise 알고리즘 (외적 활용)

#include<iostream>

using namespace std;

void ccw(int x1, int x2, int x3, int y1, int y2, int y3) {
	int res = x1 * y2 + x2 * y3 + x3 * y1;
	res += (-y1 * x2 - y2 * x3 - y3 * x1);

	if (res > 0)
		cout << 1;
	else if (res < 0)
		cout << -1;
	else
		cout << 0;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int x1, x2, x3, y1, y2, y3;
	cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

	ccw(x1, x2, x3, y1, y2, y3);

	return 0;
}