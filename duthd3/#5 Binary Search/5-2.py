n, m = map(int, input().split())
length = list(map(int, input().split()))#떡 길이들의 배열

result = 0
length.sort()

def b_search(array, s, e, target):
    global mid # 절단기의 높이
    
    if s == e:
        return mid
    mid = (s + e) // 2
    result = 0 #잘라낸 떡의 길이의 합
    for i in length:
        if i - mid >= 0:
            result += i - mid
    #더 많이 잘라 냈을때
    if result > target: # 잘라낸 떡의 길이가 target보다 클때, 즉 start를 올려야 한다.
        b_search(array, mid+1, e, target)
    else: # 덜 잘라 냈을 때
        b_search(array,s, mid-1, target)       
        
    return mid  
  
print(b_search(length, 0, max(length), m))