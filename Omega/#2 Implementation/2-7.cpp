#include <bits/stdc++.h>

using namespace std;

string s;
int ans=1000; // �Է� �� �� �ִ� �ִ� ���ڿ� ���� == MAX_VALUE

int solution(string s) {
	for (int i = 1; i <= s.size()/2; i++) { // ���ݱ����� ��, ���� �̻� ���̸� ���ϴ� �� �ǹ� X
		int cnt = 1; // �� �� �ݺ��Ǿ��� �� Ȯ��
		string res = ""; // ���� ��ȭ�� ���ڿ�
		string ss = s.substr(0, i); // abcabcd �� ���� �� 0��°���� i����ŭ ����

		for (int j = i; j <= s.size(); j+=i) { // �� �ں��� �˻� ����
			// i�� ��ŭ ������ cnt ����
			if (ss == s.substr(j, i)) {
				cnt += 1;
			}
			// �ٸ� �� cnt�� 1�̸� �ѹ��� �ݺ��� �� -> �׳� res�� ������ �͸� �����ֱ�
			else {
				if (cnt == 1) {
					res += ss;
				}
				// 1�� �ƴϸ� �ݺ��� ���� cnt + ss�� res�� �ٿ���
				else {
					res += (to_string(cnt)) + ss;
				}
				// �� �� �� �ڸ����� i����ŭ�� ���ο� �������� ���
				ss = s.substr(j, i);
				cnt = 1;
			}
		}
		// s.size() �� i���� �� �������� ��� -> �� ���� ���� �κ��� �׳� res�� ���ϱ�
		if ((s.size() % i) != 0) {
			res += s.substr((s.size() / i) * i);
		}
		// ans�� res�� ���� ��
		if (ans > res.size()) {
			ans = res.size();
		}
	}
	// ans ��ȯ
	return ans;
}

int main() {
	cin >> s;
	cout << solution(s)<<"\n";
	return 0;
}
// aabbaccc
// ababcdcdababcdcd
// abcabcdede
// abcabcabcabcdededededede