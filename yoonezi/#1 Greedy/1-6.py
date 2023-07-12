arr = input()

#입력받은 문자열(arr)의 첫번째 값[0[을 정수로 변환하여 저장
result = int(arr[0])

#arr의 [1]번째 배열부터 시작
for i in range(1, len(arr)):
    #정수로 변환
    num = int(arr[i])
    if num <= 1 or result <= 1 :
        result += num
    else:
        result *= num
print(result)