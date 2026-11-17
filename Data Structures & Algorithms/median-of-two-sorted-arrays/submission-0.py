class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        i: int = 0
        j: int = 0

        med1: int = 0
        med2: int = 0

        counter = 0
        while counter < (n1 + n2) // 2 + 1:
            med2 = med1
            if i < n1 and j < n2:
                if nums1[i] < nums2[j]:
                    med1 = nums1[i]
                    i += 1
                
                else:
                    med1 = nums2[j]
                    j += 1

            elif i < n1:
                med1 = nums1[i]
                i += 1
            else:
                med1 = nums2[j]
                j += 1

            counter += 1

        print(i, j)

        if (n1 + n2) % 2 != 0:
            return med1

        else: 
            return (med1 + med2) / 2

        return 1.0



        