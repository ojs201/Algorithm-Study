n = int(input())
data = list(map(int, input().split()))
data.sort()


result = 0 #그룹 수
count = 0 #그룹의 인원 수

for i in data:
    count += 1
    if (count >= i):#그룹의 인원이 공포도 이상일 경우
        result += 1 #그룹결성
        count = 0 
print(result)



