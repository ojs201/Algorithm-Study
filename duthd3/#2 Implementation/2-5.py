data = input()
length = len(data)

p_sum = 0
l_sum = 0

for i in range(length//2):
    p_sum += int(data[i])
    l_sum += int(data[-(i+1)])

if p_sum == l_sum :
    print("LUCKY")
else:
    print("READY")