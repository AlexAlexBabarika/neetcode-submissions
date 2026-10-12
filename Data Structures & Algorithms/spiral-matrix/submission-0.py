class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        offset_n = 0
        offset_s = 0
        offset_w = 0
        offset_e = 0

        movement = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]


        rows = len(matrix)
        cols = len(matrix[0])
        n = rows * cols

        spiral = [0] * n
        mov_type = 0
        counter = 0
        x = -1
        y = 0
        while counter < n:
            print(counter, mov_type)
            x += movement[mov_type][0]
            y += movement[mov_type][1]

            print(f"x:{x}, y:{y}")

            spiral[counter] = matrix[y][x]
            counter += 1

            if mov_type == 0 and x == cols - offset_e - 1:
                mov_type += 1
                # offset_e += 1
                offset_n += 1
                continue

            if mov_type == 1 and y == rows - offset_s - 1:
                mov_type += 1
                # offset_s += 1
                offset_e += 1
                continue

            if mov_type == 2 and x == offset_w:
                mov_type += 1
                # offset_w += 1
                offset_s += 1
                continue
            
            if mov_type == 3 and y == offset_n:
                print("Offset_n")
                print("Switching from 3")
                mov_type = 0
                # offset_n += 1
                offset_w += 1
                continue

        return spiral
            


        