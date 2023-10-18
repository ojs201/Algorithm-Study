# 문자열 + 구현 문제

# - 첫번째부터 문자열의 절반까지만 for문으로 순회하며 압출할 길이 결정
# - 압축할 내용을 담고 있다가 한번에 숫자 + 문자 형태로 만들기
# * 압출 할 수 없을 땐 숫자없이 문자만 있도록
# - 압축 단위마다 최소값을 갱신


def solution(s):
    answer = len(s)
    # 입력된 문자열의 개수가 하나일 경우 처리
    if len(s) == 1:
        return 1
        
    # 반복되는 문자열은 최대 문자열의 반이니
    for i in range(1, len(s) // 2 + 1):
        # print("i:", i)
        cnt = 1 
        arr = '' # 문자 추가할 배열
        tmp = s[:i]
        # print('tmp:', tmp)
        for j in range(i, len(s), i):
            # print(i, len(s), i)
            # print('j:', j)
            if tmp == s[j:j+i]:
                cnt += 1
                # print(cnt)
                # print(tmp)
            else:
                if cnt == 1: # 압축 할 수 없는 경우
                    arr += tmp
                    # print(arr)
                else: # 압축 할 수 있는 경우
                    arr += str(cnt) + tmp
                    # print(arr)
                cnt = 1
                tmp = s[j:j+i] # 여기서 부터 다시 시작
                # print(tmp)
                
        if cnt == 1: # 남은 문자열 처리
            arr += tmp
            # print(arr)
        else:
            arr += str(cnt) + tmp
            # print(arr)
        answer = min(answer, len(arr)) # 계속 갱신하며 최소값 찾기
        # print(answer)
                    
    return answer


print(solution('aabbaccc'))
# print(solution('ababcdcdababcdcd'))
# print(solution('abcabcdede'))
# print(solution('abcabcabcabcdededededede'))
