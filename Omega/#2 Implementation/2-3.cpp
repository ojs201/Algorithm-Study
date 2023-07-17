#include <bits/stdc++.h>

using namespace std;

string arr;
int ans;
int dx[] = { 1,2,1,2,-1,-2,-1,-2 };
int dy[] = { -2,-1,2,1,-2,-1,2,1 };

int main() {
	cin >> arr;
	int x, y;
	int row = arr[1] - '1'; // 행, 열 숫자를 맞춰주기 위함
	int col = arr[0] - 'a';
	//cout << row << ", " << col;
	for (int i = 0; i < 8; i++) {
		x = col, y = row;
		x += dx[i];
		y += dy[i];
		if (x < 0 || y < 0 || x>7 || y>7) {
			continue;
		}
		ans++;
	}
	cout << ans << "\n";
	return 0;
}