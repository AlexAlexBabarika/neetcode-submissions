class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force
        # n = len(heights)
        # max_area = 0
        # for s in range(n):
        #     min_h = heights[s]
        #     max_area = max(max_area, heights[s])
        #     for e in range(s + 1, n):
        #         min_h = min(min_h, heights[e])
        #         # print(s, e, min_h * (e - s + 1))
        #         max_area = max(max_area, min_h * (e - s + 1))

        # non brute force
        # n = len(heights)
        # max_area = 0

        max_area = 0
        stack = []  # idx, height

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                pos, height = stack.pop()
                max_area = max(max_area, height * (i - pos))
                start = pos
            
            stack.append((start, h))

        for pos, height in stack:
            max_area = max(max_area, height * (len(heights) - pos))

        return max_area

        