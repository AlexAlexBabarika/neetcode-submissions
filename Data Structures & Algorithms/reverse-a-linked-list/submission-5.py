# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        nodeStack = []
        curr = head
        while curr:
            nodeStack.append(curr)
            curr = curr.next

        new_head = nodeStack.pop()
        curr = new_head
        while nodeStack:
            curr.next = nodeStack.pop()
            curr = curr.next

        curr.next = None

        return new_head

        