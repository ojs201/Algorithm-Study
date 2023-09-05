# 문제 요약 :    
#     - 학생들에게 0 ~ n 번호 부여
#     - 처음에는 학생들이 모두 다른 팀 : n+1 개의 팀 존재

#     - 2개의 연산 :
#         1) 팀 합치기
#             " 0 a b "
#         2) 같은 팀 여부 확인
#             " 1 a b "
            
#     > m 개의 연산, '같은 팀 여부 확인' 연산에 대한 연산 결과 출력
    
# 아이디어 :
#     1. n + 1 개의 빈 부모 테이블 생성 및 초기화
#     2. 팀 합치기 함수 생성
#     3. 부모 찾기 함수 생성
#     + 같은 팀 여부 확인 함수 생성
#     4. 입력 받을 때 마다 " 0 / 1 " 확인해서 해당 함수 실행
#     5. 출력하기
    
# > "서로소 집합 자료구조, 경로 압축" 을 사용

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_team(parent, a, b):
    if parent[a] == parent[b]:
        print("YES")
    else:
        print("NO")
    
n, m = map(int, input().split()) # 입력받기
parent = [0] * (n+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i
    
for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union_parent(parent, a, b)
    else:
        same_team(parent, a, b)