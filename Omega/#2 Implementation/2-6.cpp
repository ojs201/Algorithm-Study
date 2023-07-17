#include <bits/stdc++.h>	

using namespace std;

vector<char> v1;
int sum;

int main() {
	string s;
	cin >> s;
	for (int i = 0; i < s.length(); i++) {
		if (s[i] <= '9' && s[i] >= 0) {
			sum += s[i] - '0';
		}
		else {
			v1.push_back(s[i]);
		}
	}
	sort(v1.begin(), v1.end());
	for (auto k = v1.begin(); k != v1.end(); k++) {
		cout << *k;
	}
	cout << sum;
	return 0;
}