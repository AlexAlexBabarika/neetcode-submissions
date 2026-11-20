from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        n = len(beginWord)

        def similarity(word1, word2):
            score = 0
            for ch1, ch2 in zip(word1, word2):
                if ch1 == ch2:
                    score += 1

            return score

        # if similarity(beginWord, endWord) == n - 1: return 2

        def get_next(word):
            candidates = []
            for cand in wordList:
                if cand == word: continue
                if similarity(word, cand) == n - 1:
                    # score = similarity(beginWord, cand)
                    candidates.append(cand)

            # return sorted(candidates, key=lambda x: x[0], reverse=True)
            return candidates

        # def dfs(i, word, path):
            # if similarity(beginWord, word) == len(beginWord) - 1:
            #     return i + 1 

        #     best = float('inf')
        #     for score, cand in get_next(word):
        #         if cand in path:
        #             continue
        #         path.add(cand)
        #         best = min(best, dfs(i + 1, cand, path))
        #         path.remove(cand)
        #     return best

        queue = deque([(endWord, 1)])
        path = {endWord}
        while queue:
            word, depth = queue.popleft()

            if similarity(beginWord, word) == n - 1:
                return depth + 1

            for cand in get_next(word):
                if cand not in path:
                    queue.append((cand, depth + 1))
                    path.add(cand)


        # res = dfs(1, endWord, {endWord, beginWord})
        return 0

        """
            [
                []
            ]
        """
        