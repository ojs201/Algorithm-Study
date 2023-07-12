#그리디 알고리즘
# 각 패턴에서 가장 큰수를 최대한 활용하면서 남은 횟수에 따라 두번째로 큰수를 사용함

#입력받을 수의 개수 : n , 더할 수의 개수 : m , 최대 중복하여 더할 수 있는 개수 : k
n, m, k = map(int, input().split())

#result = []
#n개의 자연수 입력받기
arr = list(map(int, input().split()))

#입력받은 배열 내림차순 정렬
arr.sort(reverse=True)
#print(arr)

#1. 가장 큰수인 arr[0]을 k만큼 반복해서 사용
#2. 두번째로 큰수인 arr[1]을 한번 사용하고 
#3. 다시 arr[0] 번 k만큼 반복하여 사용
#4. 1~3은 m만큼 반복 
#5. 여기서, 가장큰수가 더해지는 횟수를 알아야함

max = arr[0]
next = arr[1]

#가장 큰 수 k번 + 두번째 큰수 1번 패턴으로 쓰이기 때문에 = k+1
#이 한 세트(k+1)가 총 얼마나 쓰일 수 있는지, m//(k+1) 몫 구해주고
#나머지로 나머지 횟수

count = m//(k+1) * k + m % (k+1)
result = count * max + (m-count)*next
print(result)