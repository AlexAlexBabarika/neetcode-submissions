class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks: freq[ord(t) - ord('A')] += 1

        maxFreq = max(freq)

        countMax = 0
        for f in freq: 
            if f == maxFreq:
                countMax += 1 

        print(maxFreq, countMax)
        print(freq)

        frameLength = (maxFreq - 1) * (n + 1) + countMax

        return max(len(tasks), frameLength)