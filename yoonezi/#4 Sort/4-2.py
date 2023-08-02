n = int(input())
student =  [(input().split()) for _ in range(n)]
    
student.sort(key=lambda x : x[1])
for s in student:
    print(s[0], end=' ')