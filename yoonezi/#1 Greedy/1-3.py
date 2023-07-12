# 전체탐색 알고리즘(가능한 모든 경우를 고려하여 최적의 해를 찾는 방식)
# 모든 행을 순회하고 각 행의 최소값을 구하는 모든 경우를 확인하고 있음

# n x m 형태의 카드가 있고 행을 선택 -> 선택한 행의 가장 작은 수가 모든 n개의 행의 가장 작은수보다 커야함

# 행, 열, 뽑을 행을 공백을 기준으로 입력받음
n, m =  map(int, input().split())

# n개 만큼 m개로 이루어진 카드를 입력받음

# 카드를 저정할 2차원 리스트
cards = []
# n개의 행을 입력 받음
for i in range(n):
    row = list(map(int, input().split()))
    cards.append(row)
    
# 각 행마다 가장 작은 값을 구해서 넣을 배열
min_arr = []

for row in cards: # 카드의 모든 행을 순회
    # min_num = row[0] # 초기값으로 각 행마다 가장 첫번째 열의 값
    # for num in row: # 각 행의 열을 순회
    #     if num < min_num: # 최소값 비교
    #         min_num = num
    # min_arr.append(min_num) #각 행의 열의 순회를 마치며 각 행의 최소값이 구해지면 배열에 추가 
    # #print(min_arr)
    min_num = min(row)
    min_arr.append(min_num)
    
# max_num = max(min_arr)
# print(max_num)
print(min_arr.index(max(min_arr)))