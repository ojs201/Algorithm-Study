#include <bits/stdc++.h>

using namespace std;

string s;
int lef, rig;

int main() {
	cin >> s;
	int len = s.length();
	for (int i = 0; i < len; i++) {
		if (i < len / 2) {
			lef += s[i] - '0';
		}
		else {
			rig += s[i] - '0';
		}
	}
	if (lef == rig) {
		cout << "LUCKY" << "\n";
	}
	else {
		cout << "READY" << "\n";
	}
	return 0;
}