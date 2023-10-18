def sol(n, stages):
    answer = [] #각 스테이지에서의 실패율 담는 배열
    result = [] #겨로가
    user_length = len(stages) #유저의 수
   
    for i in range(1, n + 1): #1스테이지 부터 n스테이지까지
        fail_user_count = stages.count(i)
        if user_length == 0 :
            failure = 0
        else :
            failure = fail_user_count / user_length #stage의 실패유저수 / stage의 유저 수
        
        user_length = user_length - fail_user_count #다음 stage의 유저 수를 현재 stage에서 실패한 유저수 빼줘야함
        answer.append((i, failure)) # 현재 스테이지와 실패율 append
    answer.sort(key=lambda x: -x[1]) # 실패율 기준 내림차순으로 정렬
    for a in answer:
        result.append(a[0])
    print(result)
    return result

sol(5, [2, 1, 2, 6, 2, 4, 3, 3])