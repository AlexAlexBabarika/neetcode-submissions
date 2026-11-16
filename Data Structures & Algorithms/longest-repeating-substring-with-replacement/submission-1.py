from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        max_freq = 0

        n = len(s)
        l = 0
        best = 0

        for r in range(n):
            char_freq[s[r]] += 1
            max_freq = max(char_freq[s[r]], max_freq)

            while (r - l + 1) - max_freq > k:
                char_freq[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)
        return best
        