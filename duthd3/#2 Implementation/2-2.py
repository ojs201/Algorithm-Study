data = int(input())

result = 0

for h in range(data+1):
    for m in range(60):
        for s in range(60):
            time = str(h)+str(m)+str(s)
            if '3' in time:
                result+=1

print(result)