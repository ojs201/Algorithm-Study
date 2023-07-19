#include <bits/stdc++.h>

using namespace std;

int N;
vector<int> v;

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}
	sort(v.begin(), v.end());
	int cnt = 1;
	int idx = 0;
    // 1,2,3,8
	while (1) {
		if (v[idx] > cnt) {
			break;
		}
		else {
			cnt += v[idx];
			idx++;
		}
		if (idx >= N) {
			break;
		}
	}
	cout << cnt << "\n";
	return 0;
}