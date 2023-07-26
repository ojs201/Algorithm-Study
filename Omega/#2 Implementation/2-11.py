# 치킨 배달

from itertools import combinations

n, m = map(int, input().split())
chicken = []
house = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
selected = list(combinations(chicken, m))


# 치킨 거리의 합을 계산하는 함수
def chicken_sum(selected):
    result = 0
    # 모든 집에 대하여
    for a, b in house:
        # 가장 가까운 치킨집을 찾기
        temp = 2e9
        for c, d in selected:
            temp = min(temp, abs(a - c) + abs(b - d)) # abs(a - c) + abs(b - d) = 집과 선택된 치킨집 사이의 거리
        # 각 경우에 대한 가장 가까운 치킨집까지의 거리를 모두 더하기
        result += temp
    return result


# 치킨 거리의 합의 최소를 찾아 출력
result = 2e9
for i in selected:
    result = min(result, chicken_sum((i)))

print(result)
