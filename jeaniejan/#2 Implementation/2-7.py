#문자열 압축
def solution(s):
    ans=len(s)
    for step in range(1,len(s)//2+1):
        com=""
        prev=s[0:step]
        cnt=1
        
        for i in range(step,len(s),step):
            if prev==s[i:i+step]:
                cnt+=1
            else:
                com+=str(cnt)+prev if cnt>=2 else prev
                prev=s[i:i+step]
                cnt=1
        com+=str(cnt)+prev if cnt>=2 else prev
        ans=min(ans,len(com))
    return ans