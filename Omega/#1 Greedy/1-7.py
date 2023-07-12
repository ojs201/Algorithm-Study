# 문자열 뒤집기

data = list(map(int, input()))
zero_group_num = 0
one_group_num = 0
result = 0

for i in range(0, len(data) - 1):
    if data[i] == data[i + 1]:
        if i == len(data) - 2:
            if data[i] == 0:
                zero_group_num += 1
            else:
                one_group_num += 1
    else:
        if i == len(data) - 2:
            zero_group_num += 1
            one_group_num += 1
        else:
            if data[i] == 0:
                zero_group_num += 1
            else:
                one_group_num += 1

result = one_group_num if zero_group_num > one_group_num else zero_group_num
print(result)


