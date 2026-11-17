# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        temp1 = l1
        temp2 = l2

        nums1 = []
        nums2 = []

        while temp1 or temp2:
            if temp1 and temp2:
                nums1.append(temp1.val)
                nums2.append(temp2.val)

                temp1 = temp1.next
                temp2 = temp2.next

            elif temp1:
                nums1.append(temp1.val)
                temp1 = temp1.next

            else:
                nums2.append(temp2.val)
                temp2 = temp2.next

        num1 = int("".join(map(lambda x: str(x), nums1[::-1])))
        num2 = int("".join(map(lambda x: str(x), nums2[::-1])))
        
        num = str(num1 + num2)[::-1]

        head = ListNode(num[0])
        temp = head
        counter = 1
        while counter < len(num):
            temp.next = ListNode(num[counter])
            temp = temp.next
            counter += 1

        return head