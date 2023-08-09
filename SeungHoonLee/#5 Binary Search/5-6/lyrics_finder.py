from bisect import bisect_right, bisect_left


def count_between(nums, el_left, el_right) -> int:
    return bisect_right(nums, el_right) - bisect_left(nums, el_left)


class LyricsFinder:
    MAX_WORDS = 10001

    def __init__(self, words):
        self.lyrics = self.map_lyrics(words)
        self.r_lyrics = self.map_lyrics(words, reverse=True)

    def map_lyrics(self, words, reverse=False):
        lyrics = [[] for _ in range(LyricsFinder.MAX_WORDS)]

        for word in words:
            word = word if not reverse else word[::-1]
            lyrics[len(word)].append(word)

        for i in range(LyricsFinder.MAX_WORDS):
            lyrics[i].sort()
        return lyrics

    def find_lyrics(self, queries):
        return [self.execute_query(q) for q in queries]

    def execute_query(self, q):
        n = len(q)
        words = self.lyrics[n] if q[0] != '?' else self.r_lyrics[n]
        query = q if q[0] != '?' else q[::-1]
        return count_between(words, query.replace('?', 'a'), query.replace('?', 'z'))
