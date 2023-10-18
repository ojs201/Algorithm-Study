n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort() #정렬을 해줘야 한다

def b_search(array, s, e, target):
    
    if s > e :
        return "no"
    mid = (s + e) // 2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return b_search(array, s, mid-1, target)
    else:
        return b_search(array, mid+1, e, target)
    

for i in m_list:
    print(b_search(n_list, 0, n-1, i))
   