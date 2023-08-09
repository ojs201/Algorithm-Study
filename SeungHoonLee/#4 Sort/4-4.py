"""
4-4. 국영수

다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.

1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
    - (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

- N -> 반학생의 숫자, 1 ≤ N ≤ 100,000
- 한 줄에 하나씩 각 학생의 (이름, 국어, 영어, 수학)이 공백으로 구분해 주어짐
- 점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수
- 이름은 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않음
"""
from sys import stdin


def map_to_name_and_grades(student: str) -> tuple:
    name, kor, eng, math = student.split(' ')
    return -int(kor), int(eng), -int(math), name


scores = list(map(map_to_name_and_grades, stdin.readlines()[1:]))
print(*map(lambda score: score[3], sorted(scores)), sep='\n')
