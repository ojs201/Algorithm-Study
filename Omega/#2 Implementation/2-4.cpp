#include <bits/stdc++.h>

using namespace std;

int N, M;
int MAP[50][50];
int visited[50][50];

int dx[] = { -1,0,1,0 };
int dy[] = { 0,-1,0,1 };

int ans=1; // �ϴ� ������ �����Ƿ� ���� 1���� count
int x, y, dir;

void change_dir() {
	dir++;
	if (dir == 4) {
		dir = 0;
	}
}
void go() {
	int nx, ny;
	int cnt = 0; //�� ��ġ���� �� �� ���Ҵ� ��
	// �׳� DFS (x) -> �Դ� ���� ������ �����ϰ� �־��.
	while (1) {
		change_dir(); // changed_dir -> ȸ�� ������ ��ȯ 
		nx = x + dx[dir];
		ny = y + dy[dir];
		if (visited[nx][ny] == 0 && MAP[nx][ny] == 0) { // �湮 X , MAP ���� �� ī��Ʈ
			visited[nx][ny] = 1;
			x = nx;
			y = ny;
			ans++;
			cnt = 0;
			continue;
		}
		else {
			cnt++; // �̷��� �ؼ� 4�� ȸ�� �ߴµ� �� ã���� �ٽ� ������ġ�� ���ư���
		}
		if (cnt == 4) {
			nx = x - dx[dir];
			ny = y - dy[dir];
			if (MAP[nx][ny] == 0) { // ���� �״�� ���ư��µ� ������ �ű⼭ ���� �ٽ�
				x = nx;
				y = ny;
			}
			else { // ���� �״�� ���ư��µ� �ٴٸ� break
				break;
			}
			cnt = 0;
		}
	}
}
int main() {
	cin >> N >> M;
	cin >> x >> y >> dir;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> MAP[i][j];
		}
	}
	visited[x][y] = 1;
	go();
	cout << ans << "\n";
	return 0;
}
/*
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
*/