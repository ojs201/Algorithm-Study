"""
4-6. 실패율

풀이:
1. 입력으로부터 (스테이지, 실패율)의 요소를 가지는 집합을 만든다.
2. 해당 집합에 대해 실패율 기준 내림차 순, 스테이지 번호 기준 오름차 순 정렬한다.
3. 정렬된 값을 반환한다.
"""
from analyzer import FailureRateAnalyzer


def solution(N: int, stages: list[int]) -> list:
    analyzer: FailureRateAnalyzer = FailureRateAnalyzer(N, stages)
    return analyzer.analyze()


if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
