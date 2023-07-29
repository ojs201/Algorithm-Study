"""
4-2. 성적이 낮은 순서로 학생 출력하기

- 학생의 (이름, 성적)이 주어질 때 성적이 낮은 순서대로 이름을 출력하는 문제
- 학생의 이름의 길이와 성적은 100 이하의 자연수이다.
- 성적이 동일한 학생은 순서를 자유롭게
"""
from sys import stdin


def map_to_name_and_grade(student: str) -> tuple:
    name, grade = student.split(' ')
    return name, int(grade)


items = dict(map(map_to_name_and_grade, stdin.readlines()[1:]))
print(*(sorted(items.keys(), key=items.get)))
