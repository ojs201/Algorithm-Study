# 모험가 길드

import sys

n = sys.stdin.readline().rstrip()
data = list(map(int, input().split()))
group_num = 0
count = 0

data.sort()

for i in data:
    count += 1
    if count == i:
        group_num += 1
        count = 0

print(group_num)