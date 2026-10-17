class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        dig_to_let = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        res = []
        def dfs(i, curStr):
            # print("Curr idx: ", i, "Curr str: ", curStr)
            if len(curStr) == len(digits):
                # print("Append: ", curStr)
                res.append(curStr)
                return

            if i >= len(digits):
                # print("Discard")
                return

            for ch in dig_to_let[digits[i]]:
                # curStr += ch
                dfs(i+1, curStr + ch)
                # curStr = ""

        dfs(0, "")
        return res



        # res = []
        # def backtrack(i, curStr):
        #     if len(curStr) == len(digits):
        #         res.append(curStr)
        #         return

        #     for c in dig_to_let[digits[i]]:
        #         backtrack(i + 1, curStr + c)

        # if digits:
        #     backtrack(0, "")

        return res

        