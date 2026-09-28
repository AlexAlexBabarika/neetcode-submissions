class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for c in range(len(s)):
            while s[c] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[c])
            res = max(res, c - l + 1)

        return res
        
        