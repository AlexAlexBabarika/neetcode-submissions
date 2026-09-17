class Solution:
    def longestPalindrome(self, s: str) -> int:
        N = len(s)
        if N == 1: return 1

        charmap = defaultdict(int)
        length = 0
        for c in s:
            charmap[c] += 1
            if charmap[c] % 2 == 0:
                length += 2

        for val in charmap.values():
            if val % 2:
                length += 1
                break

        print(charmap)
        
        return length

        