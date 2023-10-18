n = int(input())
levels = list(map(int, input().split()))

# 오름차순 정렬
levels.sort()
# print(levels)

group = 0
count = 0

for i in levels: # 공포 레벨을 순회하며
    count += 1 # 일단 순회하면서부터 1명씩 추가
    if count == i: # 현재 공포레벨보다 인원수가 같다면
        group += 1 # 그룹의 수를 1 증가시키고 
        count = 0 # 인원 수 0으로 초기화
        # print(i)
        # print(group, count)
    # else:
    #     count += 1 #아니면 계속 인원수 1씩 추가함
    #     print(i)
        
    #     print(group, count)
        
print(group)


# 처음엔 if count == i와 else로 하였는데
# 1 2 2 2 3 -> i = 1, count = 1 -> 1 == 1
# i = 2 , count = 1
# i = 2, count -> 2 == 2
# i = 2 , count = 1 
# i = 3, count = 2
#아 else가 필요없구나