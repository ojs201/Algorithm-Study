#include <bits/stdc++.h>

using namespace std;

int N;
string arr;
int dx[4] = { 0,-1,0,1 };
int dy[4] = { 1, 0, -1, 0 };
char dir[4] = { 'D', 'L','U','R' };

int main() {
	cin >> N;
	cin.ignore();
	getline(cin, arr);
	int x, y;
	x = y = 1;
	for (int i = 0; i < arr.length(); i++) {
		/*if (arr[i] == ' ') {
			continue;
		}*/
		for (int j = 0; j < 4; j++) {
			if (arr[i] == dir[j]) {
				x = x + dx[j];
				y = y + dy[j];
			}
			if (x <= 0 || y <= 0 || x > N || y > N) {
				x -= dx[j];
				y -= dy[j];
			}
		}
		
	}
	cout << y << "," << x << "\n";
	return 0;
}

// 5 R R R U D D