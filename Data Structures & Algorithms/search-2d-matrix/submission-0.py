class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, hr = 0, len(matrix) - 1
        lc, hc = 0, len(matrix[0]) - 1

        if target < matrix[0][0] or target > matrix[-1][-1]: return False

        row = -1

        while lr <= hr:
            mid = (lr + hr) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break

            elif target < matrix[mid][0]:
                hr = mid - 1

            elif target > matrix[mid][-1]:
                lr = mid + 1
        
        while lc <= hc:
            mid = (lc + hc) // 2

            if target == matrix[row][mid]:
                return True

            elif target < matrix[row][mid]:
                hc = mid - 1

            elif target > matrix[row][mid]:
                lc = mid + 1

        return False




        