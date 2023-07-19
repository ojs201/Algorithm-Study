# 볼링공 고르기

n, m = map(int, input().split())
data = list(map(int, input().split()))
count = 0

data.sort()  #오름차순 정리


for i in range(0, len(data) - 1):
    for j in range(i + 1, len(data)):
        if data[i] < data[j]:  # i + 1번째로 작은 수보다 큰 수가 몇 개인지 찾기
            count += 1
        else:
            continue

print(count)


"""
n,m = map(int,input().split())
arr = list(map(int,input().split()))
 
# 인덱스에 해당하는 무게를 가지는 볼링공 수 저장. M은 최대 10
array = [0] * 11 
for i in arr:
  array[i] += 1
 
result = 0
for i in range(1,m+1): # a가 선택하는 무게
  n -= array[i] # b가 선택하는 경우의 수. 무게가 i인 볼링공의 개수 제외, 이미 선택한건 계속 빠짐
  result += array[i]*n # a가 선택하는 경우의 수 * b가 선택하는 경우의 수
 
print(result)
"""





