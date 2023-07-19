#include <bits/stdc++.h>

using namespace std;

int N, M;
int MAP[50][50];
int visited[50][50];

int dx[] = { -1,0,1,0 };
int dy[] = { 0,-1,0,1 };

int ans=1; // 일단 육지에 있으므로 답은 1부터 count
int x, y, dir;

void change_dir() {
	dir++;
	if (dir == 4) {
		dir = 0;
	}
}
void go() {
	int nx, ny;
	int cnt = 0; //현 위치에서 몇 번 돌았는 지
	// 그냥 DFS (x) -> 왔던 방향 정보를 유지하고 있어야.
	while (1) {
		change_dir(); // changed_dir -> 회전 방향을 전환 
		nx = x + dx[dir];
		ny = y + dy[dir];
		if (visited[nx][ny] == 0 && MAP[nx][ny] == 0) { // 방문 X , MAP 육지 시 카운트
			visited[nx][ny] = 1;
			x = nx;
			y = ny;
			ans++;
			cnt = 0;
			continue;
		}
		else {
			cnt++; // 이렇게 해서 4번 회전 했는데 못 찾으면 다시 이전위치로 돌아가기
		}
		if (cnt == 4) {
			nx = x - dx[dir];
			ny = y - dy[dir];
			if (MAP[nx][ny] == 0) { // 방향 그대로 돌아갔는데 육지면 거기서 부터 다시
				x = nx;
				y = ny;
			}
			else { // 방향 그대로 돌아갔는데 바다면 break
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