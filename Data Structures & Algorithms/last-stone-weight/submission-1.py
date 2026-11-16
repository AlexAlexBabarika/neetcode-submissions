import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            st1 = heapq.heappop(stones)
            st2 = heapq.heappop(stones)

            if st1 == st2: continue
            elif st1 > st2:
                heapq.heappush(stones, st2 - st1)
            else: 
                heapq.heappush(stones, st1 - st2)


        return 0 if not stones else -stones[0]