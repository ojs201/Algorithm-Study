def solution(s):
    cnt1 = ""
    cnt2 = ""
    answer = ""
    length = len(s)
    half_len = len(s) // 2 + 1
    
    for i in range(half_len):
        cnt1 += s[i]
    
    for j in range(half_len, length):
        cnt2 += s[j]
        
    if cnt1 == cnt2:
        answer = "LUCKY"

    answer = "READY"
    
    return answer

print(solution("123402"))
