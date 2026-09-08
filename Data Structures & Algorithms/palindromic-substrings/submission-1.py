class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        if n == 1: return 1

        count = 0
        for ch in range(len(s)):
            left, right = ch, ch
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                # if right - left + 1 > length:
                #     length = right - left + 1
                #     start = left

                left -= 1
                right += 1

            left, right = ch, ch + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1

                # if right - left + 1 > length:
                #     length = right - left + 1
                #     start = left

                left -= 1
                right += 1

        return count
        