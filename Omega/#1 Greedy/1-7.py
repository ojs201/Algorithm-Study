# 문자열 뒤집기

"""
data = list(map(int, input()))
cnt0 = 0
cnt1 = 0
result = 0

for i in range(0, len(data) - 1):
    if data[i] == data[i + 1]:
        if i == len(data) - 2:
            if data[i] == 0:
                cnt0 += 1
            else:
                cnt1 += 1
    else:
        if i == len(data) - 2:
            cnt0 += 1
            cnt1 += 1
        else:
            if data[i] == 0:
                cnt0 += 1
            else:
                cnt1 += 1

result = cnt1 if cnt0 > cnt1 else cnt0
print(result)
"""


#다른 방법
data = list(input())
cnt0 = 0
cnt1 = 0

# 바뀌는 구간이 1번만 있는 경우를 고려. ex) 00100인 경우
if data[0] == '0':
    cnt1 += 1
else:
    cnt0 += 1

# 현재 문자가 다음 문자와 다를 때, 현재문자가 0이면 0에서 1로 바뀐다는 의미이므로 cnt0에 1을 더함
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i] == '0':
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))

# 팀원 풀이
"""
s=input()
s=list(s)
cnt=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        cnt+=1 
print(cnt//2)
"""


