class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        lenp = len(p)

        res = []

        m = 0

        anagram_dict = {}
        for c in p:
            if c not in anagram_dict:
                anagram_dict[c] = 1
            else:
                anagram_dict[c] += 1

        def check_dict_all_zero(dictionary):
            for k in dictionary:
                if dictionary[k] > 0 or dictionary[k] < 0:
                    return False

            return True

        while m < n:
            if m + 1 >= lenp and s[m] in anagram_dict:
                print("Found at: ", m)
                left = m
                copy_dict = anagram_dict.copy()

                # copy_dict[s[m]] -= 1
                # left 

                while left > m - len(p):
                    print(left, copy_dict)

                    if s[left] in copy_dict:
                        copy_dict[s[left]] -= 1

                    else:
                        break

                    if copy_dict[s[left]] < 0:
                        break

                    left -= 1

                print(copy_dict)

                if check_dict_all_zero(copy_dict):
                    print("all zero")
                    res.append(left + 1)

            m += 1

        return res
                    


                


