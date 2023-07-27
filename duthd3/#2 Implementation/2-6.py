data = list(input())

num_result = 0
str_result = []
for num in data:
    if num.isdigit():
        num_result += int(num)
    else:
        str_result.append(num) 

str_result.sort()
print(''.join(str_result) + str(num_result))