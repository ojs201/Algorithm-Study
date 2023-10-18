n = int(input())
stu_info = []
for i in range(n):
    a, b, c, d = list(input().split()) #이름, 국어, 영어, 수학
    info = a, int(b), int(c), int(d) 
    stu_info.append(info)


# 국어 점수가 감소하는 순서
stu_info.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(stu_info[i][0])