class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        h = len(image)
        w = len(image[0])
        locked = [[0] * w for i in range(h)]
        def paintPixel(image: List[List[int]], locked, sr: int, sc: int, val: int, color: int):
            if not ((0 <= sr < h) and (0 <= sc < w)): 
                # print(f"{sr} {sc} skip")
                return
            if locked[sr][sc]: return 
            if image[sr][sc] != val: return

            locked[sr][sc] = 1
            image[sr][sc] = color 
            # for y in range(min(0, sr - 1), max(h, sr + 1)):
            #     for x in range(min(0, sc - 1), max(w, sc + 1)):
            #         if y == sr and x == sc: continue
            #         paintPixel(image, y, x, val, color)

            paintPixel(image, locked, sr - 1, sc, val, color)
            paintPixel(image, locked, sr, sc - 1, val, color)
            paintPixel(image, locked, sr, sc + 1, val, color)
            paintPixel(image, locked, sr + 1, sc, val, color)
        
        
        paintPixel(image, locked, sr, sc, image[sr][sc], color)
        return image
