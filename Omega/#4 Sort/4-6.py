# 실패율
import sys

N = int(sys.stdin.readline().rstrip())
stages = list(map(int, input().split()))
denominator = len(stages)
answer = []

for i in range(1, N + 1):
    if denominator == 0:
        answer.append((i, 0))
    else:
        fail_rate = stages.count(i) / denominator
        denominator -= stages.count(i)
        answer.append((i, fail_rate))

answer = sorted(answer, key = lambda x : x[1], reverse = True)
answer = [i[0] for i in answer]

print(answer)