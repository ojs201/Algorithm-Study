#외벽점검
import itertools
import math
def solution(n,weak,dist):
    weakSize=len(weak)
    weak=weak+[w+n for w in weak]
    minCnt=math.inf
    for start in range(weakSize):
        for d in itertools.permutations(dist,len(dist)):
            cnt=1 #투입되는 친구수
            pos=start
            for i in range(1,weakSize):
                nextPos=start+i #다음 방문할 위치
                diff=weak[nextPos]-weak[pos] #거리
                if diff>d[cnt-1]:
                    pos=nextPos
                    cnt+=1
                    if cnt>len(dist):
                        break
            if cnt<=len(dist):
                minCnt=min(minCnt,cnt)
    if minCnt==math.inf: #찾지못한 경우
        return -1
                
    return minCnt
    