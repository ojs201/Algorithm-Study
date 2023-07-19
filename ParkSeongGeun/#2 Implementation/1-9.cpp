#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int> v;
int ans;

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}
	int len = v.size();
	//sort(v.begin(), v.end());	
	for (int i = 0; i < len; i++) {
		for (int j = i + 1; j < len; j++) {
			if (v[i] != v[j]) {
				ans++;
			}
		}
	}
	cout << ans << '\n';
	return 0;
}