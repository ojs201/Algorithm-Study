def solution(s):
    num = 0
    answer = []
    
    for i in s:
        if i.isalpha():
            answer.append(i)
        else:
            num += int(i)
    
    answer.sort()
    answer.append(str(num))
    
    return ''.join(answer)

print(solution("K1KA5CB7"))