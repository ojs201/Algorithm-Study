#include <bits/stdc++.h>

using namespace std;

int N;
int ans;

int main() {
	cin >> N;
	for (int i = 0; i <= N; i++) {
		for (int j = 0; j < 60; j++) {
			for (int k = 0; k < 60; k++) {
				if (i % 10 == 3 || j % 10 == 3 || k % 10 == 3 || j / 10 == 3 || k / 10 == 3) {
					ans++;
				}
			}
		}
	}
	cout << ans << "\n";
	return 0;
}