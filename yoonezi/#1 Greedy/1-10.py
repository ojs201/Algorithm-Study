아이디어: (food_time, 음식 번호)를 heap에 넣고 food_time이 짧은 음식부터 삭제

1. 모든 음식에 대해 (food_time, 음식 번호)를 heap에 삽입한다. 

2. food_time이 짧은 음식부터 음식을 먹는데 걸리는 시간을 계산한다. 

   - 음식을 먹는데 걸리는 시간: (남은 음식 양) * (남은 음식 개수)

   - 남은 음식 양: 현재 food_time - 이전에 제거한 food_time

3. 현재 음식을 다 먹을 수 있는 경우 음식을 제거한다. 
   - 남은 시간(k)에서 현재 음식을 먹는 시간을 뺀다. 

   - 이전에 제거한 food_time과 남은 음식 개수를 갱신한다. 

4. 현재 음식을 다 먹을 수 없는 경우 남은 음식 중에서 다음에 먹어야 할 음식 번호를 구한다. 

   - heap에 남아있는 음식 번호 중에 (k + 1)번째 번호를 찾는다. 
   - k는 남아 있는 음식 개수보다 클 수 있으므로 (k % 남은 음식 개수)로 번호를 찾는다. 

 

import heapq

def solution(food_times, k):
    # answer를 못 구할 경우 -1 
    answer = -1
    # 힙 리스트
    hq = []
    # 힙리스트에 (섭취 시간, 순번)을 넣어준다.
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i+1))      
    length = len(hq)     # 음식 갯수 (한 사이클) 
    pre = 0  # 전 음식의 섭취 시간
    while hq:   # 리스트가 빌때까지
        # 가장 적은 섭취시간과 전 음식시간의 섭취시간을 빼주고, 음식 갯수를 곱해준다.
        diff = (hq[0][0] - pre) * length
        # 한사이클의 음식량을 빼줄 diff가 k보다 작거나 같으면 빼준다.
        if diff <= k:
            k -= diff
            # 한사이클을 돌렸기 때문에 해당 음식은 다먹었으니 제외 시킨다.
            length -= 1
            # 음식을 리스트에서 제외시키고, 해당 순서의 섭취시간을 변수에 업데이트 해준다.
            pre, _ = heapq.heappop(hq)
        # 한 사이클을 돌리지 못할때    
        else:
            # 한사이클을 돌리지 못하기 때문에 k와 남은 음식의 개수를 나눈 나머지가 해당 인덱스가 된다.
            idx = k % length
            # 현재 리스트가 섭취시간으로 정렬되어 있어서 두번째 값인 순번으로 정렬해준다.
            hq.sort(key = lambda x: x[1])
            # 답을 찾아주고 멈춰준다
            answer = hq[idx][1]
            break
    return answer