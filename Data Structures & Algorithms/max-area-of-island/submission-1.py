class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        lock_map = [[False] * width for x in range(height)]
        def dfs(y, x):
            if y < 0 or y >= height: return 0
            if x < 0 or x >= width: return 0
            if grid[y][x] != 1: return 0
            if lock_map[y][x]: return 0

            lock_map[y][x] = True

            return 1 + dfs(y-1, x) + dfs(y+1, x) + dfs(y, x-1) + dfs(y, x + 1)
        
        maxArea = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1 and not lock_map[y][x]:
                    maxArea = max(maxArea, dfs(y, x))

        return maxArea
        