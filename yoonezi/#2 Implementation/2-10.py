# 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 합니다.

# 규칙을 확인하는 함수 + 이를 사용하는 메인 함수

# 현재까지 결과 구조물을 모두 설치할 수 있는지 확인
def possible(result):
    # 현재까지 결과 구조물 다시 확인
    for structure in result:
        # result 리스트에서 각 명령어를 튜플 형대로 가져와서 해당 변수에 할당함
        x, y, a = structure
        
        # 설치 구조물이 기둥이라면
        if ( a == 0 ):
            if ( y == 0 # 바닥 위에 있는 경우
                or [x-1, y, 1] in result # 왼쪽에 보가 있는 경우
                or [x, y, 1] in result # 오른쪽에 보가 있는 경우
                or [x, y-1, 0] in result): # 아래에 다른 기둥이 있는 경우
                continue
            else:
                return False
        
        # 설치 구조물이 보라면
        else:
            if ([x, y-1, 0] in result # 왼쪽 끝 부분이 기둥 위에 있는 경우
                or [x+1, y-1, 0] in result # 보의 오른쪽 끝 부분이 기둥 위에 있는 경우
                or ([x-1, y, 1] in result and [x+1, y, 1] in result)): # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있는 경우
                continue
            else:
                return False
            
    return True


    
def solution(n, build_frame):
    # 결과 구조물
    result = []
    
    for command in build_frame:
        # build_frame 리스트에서 각 명령어를 튜플 형대로 가져와서 해당 변수에 할당함
        x, y, a, b = command
        
        # 설치일 떄 (b == 1)
        if (b == 1):
            # 결과 구조물에 현재 구조물 추가
            result.append([x, y, a])
            # 현재 구조물을 추가할 수 있는지 확인
            if (possible(result)):
                continue
            # 현재 구조물을 추가할 수 없다면 결과 구조물에서 제거
            else:
                result.remove([x, y, a])
        
        # 삭제라면   
        else:
            # 결과 구조물에서 현재 구조물 제거
            result.remove([x, y, a])
            # 현재 구조물을 제거할 수 있는지 확인
            if(possible(result)):
                continue    
            # 현재 구조물을 제거할 수 없다면 결과 구조물에 다시 추가
            else:
                result.append([x, y, a])
        
    return sorted(result)

