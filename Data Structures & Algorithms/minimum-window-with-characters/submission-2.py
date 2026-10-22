class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = {}
        for ch in t:
            if ch not in needed:
                needed[ch] = 0
            needed[ch] += 1

        missing = len(t)
        left = 0
        best_start, best_len = 0, float("inf")

        for i, ch in enumerate(s):
            if ch in needed:
                if needed[ch] > 0:
                    missing -= 1
                needed[ch] -= 1

            while missing == 0:
                if i - left + 1 < best_len:
                    best_len = i - left + 1
                    best_start = left

                if s[left] in needed:
                    needed[s[left]] += 1
                    if needed[s[left]] > 0:
                        missing += 1

                left += 1
        
        return s[best_start:best_start+best_len] if best_len != float("inf") else ""


