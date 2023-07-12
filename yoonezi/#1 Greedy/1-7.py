# 1. 전부 0으로 바꾸는 경우
# 2. 전부 1로 바꾸는 경우 
# 1과 2중 더 적은 횟수를 가진 경우 출력

arr = input()

count0 = 0 #0으로 뒤집기
count1 = 0 #1로 뒤집기

#첫번째 숫자에 대한 처리
if arr[0] == '1':
    count0 = 1
else:
    count1 = 1

for i in range (len(arr)-1):
    if arr[i] != arr[i+1]:
        if arr[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
        
print(min(count0,count1))