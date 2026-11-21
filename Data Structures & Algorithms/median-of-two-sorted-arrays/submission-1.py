import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        minh = []
        maxh = []

        i = 0
        j = 0
        iturn = True
        while i < n1 or j < n2:
            if i < n1 and j < n2:
                to_push = -nums1[i] if iturn else -nums2[j]
                heapq.heappush(minh, to_push)
                heapq.heappush(maxh, -heapq.heappop(minh))
                if len(maxh) > len(minh):
                    heapq.heappush(minh, -heapq.heappop(maxh))

                if iturn: i += 1
                else: j += 1

                iturn = not iturn

            elif i < n1:
                heapq.heappush(minh, -nums1[i])
                heapq.heappush(maxh, -heapq.heappop(minh))
                if len(maxh) > len(minh):
                    heapq.heappush(minh, -heapq.heappop(maxh))

                i += 1

            else:
                heapq.heappush(minh, -nums2[j])
                heapq.heappush(maxh, -heapq.heappop(minh))
                if len(maxh) > len(minh):
                    heapq.heappush(minh, -heapq.heappop(maxh))

                j += 1

        print(minh, maxh)
        if len(minh) > len(maxh):
            return -minh[0]
        else:
            return (-minh[0] + (maxh[0])) / 2




        