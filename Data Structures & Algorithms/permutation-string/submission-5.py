from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2: return False
        n1_count = Counter(s1)

        for l in range(n2 - n1 + 1):
            n2_count = Counter(s2[l:l+n1])
            if n2_count == n1_count: return True

        return False
        