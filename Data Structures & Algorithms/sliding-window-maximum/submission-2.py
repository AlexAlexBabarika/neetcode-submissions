import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for i, n in enumerate(nums):
            while heap and i - heap[0][1] >= k:
                # print("pop")
                heapq.heappop(heap)            
            heapq.heappush(heap, (-n, i))

            if i >= k - 1:
                res.append(-heap[0][0])

            # print(i, heap)

        return res
        