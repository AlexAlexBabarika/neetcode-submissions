# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        idx_to_node = {}

        temp = head
        n = 0
        while temp:
            idx_to_node[n] = temp
            temp = temp.next

            n += 1
        
        temp = head
        for i in range(1, n // 2 + 1):
            temp.next = idx_to_node[n - i]
            temp = temp.next
            temp.next = idx_to_node[i]
            temp = temp.next

        temp.next = None

        