n, k = map(int, input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))
# print(a, b)

a_arr.sort()
b_arr.sort(reverse=True)
# print(a_arr, b_arr)

cnt = 0

for a in a_arr:
    for b in b_arr:
        if cnt > k:
            break
        if a < b:
            a, b = b, a
            cnt += 1
            
# print(cnt)
# print(a_arr, b_arr)
print(sum(a_arr))