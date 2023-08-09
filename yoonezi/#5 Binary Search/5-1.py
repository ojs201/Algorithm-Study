

# ================================================

# # 동빈이네 전자 매장에 있는 부품의 개수
# n = int(input())
# # 동빈이네 부품의 고유한 번호
# n_arr = list(map(int, input().split()))
# # 손님이 요청한 부품읙 개수
# m = int(input())
# # 손님이 요청한 부품읙 고유한 번호
# m_arr = list(map(int, input().split()))


# 손님이 요청한 부품의 고유한 번호 리스트를 순회하며 
# 동빈이네 부품의 고유 번호에 있다면 yes, 
# 없다면 no 
# -> 이게 이진탐색이라고 ?

# for mm in m_arr:
#     if mm in n_arr:
#         print("yes", end =' ')
#     else:
#         print("no", end =' ')

# ================================================

# 이진 탐색 이용하기

def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            # print("yes", end = ' ')
            return 1
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right =  mid - 1
        # else:
            # print("no", end = '')
    return 0


# 동빈이네 전자 매장에 있는 부품의 개수
n = int(input())
# 동빈이네 부품의 고유한 번호
n_arr = list(map(int, input().split()))
# 손님이 요청한 부품읙 개수
m = int(input())
# 손님이 요청한 부품읙 고유한 번호
m_arr = list(map(int, input().split()))

for mm in m_arr:
    result = binary_search(n_arr, 0, n-1, mm)
    if result:
        print("yes", end =' ')
    else:
        print("no", end =' ')