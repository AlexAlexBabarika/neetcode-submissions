class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles): return max(piles)

        min_k = 1
        max_k = max(piles)

        best = float("inf")

        while min_k <= max_k:
            mid = (min_k + max_k) // 2

            time = 0
            for p in piles:
                time += math.ceil(p / mid)

            if time > h:
                min_k = mid + 1
            else:
                max_k = mid - 1
                best = min(best, mid)

        return best