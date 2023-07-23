# 알고리즘 :
#     1. 집과 치킨 좌표를 각각 리스트에 저장
#     2. m개의 치킨집을 선택하는 모든 조합에 대해 도시의 치킨 거리를 구함
#     -> itertools의 combinations 사용
#     3. 치킨 거리 절댓값 
#     -> abs() 사용
from itertools import combinations

n,m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

home = [] 
chicken = []

for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            home.append((r,c))
        elif city[r][c] == 2:
            chicken.append((r,c))
            
# 치킨 거리 찾기 함수 
def chicken_dist(home, chicken):
    dist = 0
    for r, c in home:
        dist += min(abs(r-ch_r) + abs(c-ch_c) for ch_r, ch_c in chicken)
    return dist


answer = float("inf")  # 양의 무한대
for selected in combinations(chicken, m):
    answer = min(answer, chicken_dist(home, selected))
        
print(answer)