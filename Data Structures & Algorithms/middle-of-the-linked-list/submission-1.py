# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next = head
        counter = 0

        while next:
            counter += 1
            next = next.next

        counter = (counter / 2) - (counter % 2)

        while counter  > 0:
            head = head.next
            counter -= 1

        return head

        