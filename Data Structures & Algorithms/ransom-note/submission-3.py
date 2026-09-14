class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomMap = {}
        for c in ransomNote:
            if c not in ransomMap: ransomMap[c] = 1
            else: ransomMap[c] += 1

        for c in magazine:
            if c in ransomMap: ransomMap[c] -= 1

        for v in ransomMap.values(): 
            if v > 0: return False

        return True
        