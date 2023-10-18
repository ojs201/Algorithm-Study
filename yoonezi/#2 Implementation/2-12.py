# 알고리즘 :
# weak을 순회하며 모든 dist의 조합의 경우를 순회 > 최소값 구하기
# 순열을 활용하여 모든 경우의 수 고려

import math
import itertools
 
def solution(n, weak, dist):
    weak_size = len(weak)
    # 외벽의 길이를 2배로 늘림 > 1 = 13, 2 = 14 .. 방향 고려 필요 x
    weak = weak + [w + n for w in weak]
    
    # 최소값을 가장 크게 초기화
    min_count = math.inf
    
    for start in range(weak_size):
        for d in itertools.permutations(dist, len(dist)): # dist의 모든 경우의 수 
            cnt = 1 # 투입되는 인원 수
            pos = start # weak를 순회하며 해당 순회 값이 시작 위치가 됨
            for i in range(1, weak_size): 
                next_pos =  start + i 
                diff =  weak[next_pos] - weak[pos]
                if diff > d[cnt-1]:
                    pos = next_pos
                    cnt += 1
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
        
                min_count = min(min_count, cnt)
    if min_count == math.inf:
        return -1
    else:
        return min_count