#성적이 낮은 순서로 학생 출력하기
n=int(input())
arr=[]
for i in range(n):
    arr.append(input().split())
    
arr=sorted(arr,key=lambda data:data[1])
    
for student in arr:
    print(student[0], end=' ')
    