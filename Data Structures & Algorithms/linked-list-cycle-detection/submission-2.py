# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head
        while curr:
            # print([x.val for x in visited])
            if curr not in visited:
                visited.add(curr)
            else: 
                return True

            curr = curr.next

        return False