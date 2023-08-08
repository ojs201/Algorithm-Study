"""
5-6. 가사 검색
https://school.programmers.co.kr/learn/courses/30/lessons/60060

풀이:
1. 기존 가사의 단어를 정렬한다.
2. 각 검색 키워드를 수행한다.
3. 각 검색 키워드에 매치되는 단어의 수를 구한다.

- 검색 키워드에 매치되는 단어를 찾을 때는 lower_bound, upper_bound를 이용한다.
- 구체적인 과정은 아래와 같다.

1. 검색 키워드의 접두사에 '?'이 붙어있는 경우:
    1-1. 검색 키워드의 전체 길이와 동일한 가사 단어들을 구한다.
    1-2. 검색 키워드가 해당 단어들에 얼마나 포함되어 있는지를 upper-bound, lower-bound를 이용해 구한다.
    1-3. 이때 파이썬에서 제공하는 bisect_left(=lower_bound), bisect_right(upper_bound)를 사용한다.

2. 검색 키워드의 접미사로 '?'이 붙어있는 경우:
    2-1. 검색 키워드의 전체 길이와 동일한 (뒤집힌) 가사 단어들을 구한다.
    2-2. 검색 키워드의 알파벳 순서를 뒤집는다.
    2-3. 1-2~3 과정과 동일

---

Lower bound
- 찾고자 하는 값 이상이 처음 나오는 위치
Upper bound
- 찾고자 하는 값보다 큰 값이 처음 나오는 위치

e.g.
arr = [1, 1, 2, 2, 3, 4, 4, 4, 6], k = 4
- bisect_left(arr, k) = 5
- bisect_right(arr, k) = 8
"""
from lyrics_finder import LyricsFinder


def solution(words, queries):
    finder = LyricsFinder(words)
    return finder.find_lyrics(queries)


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))
