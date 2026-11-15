# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        length: int = 0

        temp = head

        while temp != None:
            temp = temp.next
            length += 1

        n = length - n

        if n == 0:
            head = head.next
            return head
        
        prev = None
        temp = head

        while n > 0:
            prev = temp
            temp = temp.next
            n -= 1

        prev.next = temp.next

        return head