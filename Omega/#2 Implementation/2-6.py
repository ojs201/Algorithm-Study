# 문자열 재정렬
from curses.ascii import isalpha

data = str(input())
alpha = ''
digit = ''
digit_sum = 0

for i in range(len(data)):
    if data[i].isalpha() == True:
        alpha += data[i]
    else:
        digit += data[i]

for i in digit:
    digit_sum += int(i)

sorted_alpha = ''.join(sorted(alpha))

print(sorted_alpha + str(digit_sum))





