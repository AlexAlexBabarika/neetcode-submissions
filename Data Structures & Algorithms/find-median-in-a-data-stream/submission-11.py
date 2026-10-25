import heapq


class MedianFinder:
    # Check if meatcode works

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, -num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 != 0:
            return -self.min_heap[0]
        else:
            return (-self.min_heap[0] + self.max_heap[0]) / 2