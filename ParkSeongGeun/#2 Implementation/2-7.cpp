#include <bits/stdc++.h>

using namespace std;

string s;
int ans=1000; // 입력 될 수 있는 최대 문자열 길이 == MAX_VALUE

int solution(string s) {
	for (int i = 1; i <= s.size()/2; i++) { // 절반까지만 비교, 절반 이상 길이를 비교하는 건 의미 X
		int cnt = 1; // 몇 번 반복되었는 지 확인
		string res = ""; // 최종 변화된 문자열
		string ss = s.substr(0, i); // abcabcd 가 있을 떄 0번째부터 i개만큼 추출

		for (int j = i; j <= s.size(); j+=i) { // 그 뒤부터 검사 시작
			// i개 만큼 같으면 cnt 증가
			if (ss == s.substr(j, i)) {
				cnt += 1;
			}
			// 다를 때 cnt가 1이면 한번만 반복된 것 -> 그냥 res에 추출한 것만 더해주기
			else {
				if (cnt == 1) {
					res += ss;
				}
				// 1이 아니면 반복된 개수 cnt + ss를 res에 붙여줌
				else {
					res += (to_string(cnt)) + ss;
				}
				// 그 후 그 자리부터 i개만큼을 새로운 기준으로 삼기
				ss = s.substr(j, i);
				cnt = 1;
			}
		}
		// s.size() 가 i개씩 안 끊어지는 경우 -> 맨 끝에 남은 부분은 그냥 res에 더하기
		if ((s.size() % i) != 0) {
			res += s.substr((s.size() / i) * i);
		}
		// ans와 res의 길이 비교
		if (ans > res.size()) {
			ans = res.size();
		}
	}
	// ans 반환
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