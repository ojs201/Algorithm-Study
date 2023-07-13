#1-7
# 0으로 뒤집는 횟수
count0 = 0
# 1로 뒤집는 횟수
count1 = 0


data = input()
length = len(data)

if data[0] == '1' : #첫번째 원소에 대하여
    count0 += 1
else:
    count1 += 1
print(count0, count1)
for i in range(length-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1': #
            count0 += 1
            print(count0, count1)
        else:
            count1 += 1
            print(count0, count1)    
print(min(count0, count1))
                         
        
        
        
        