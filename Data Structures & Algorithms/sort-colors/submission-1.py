class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def insertionSort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1

                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

        insertionSort(nums)
        