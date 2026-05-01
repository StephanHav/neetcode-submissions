# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = None
        curr = head

        steps = 0
        while curr:
            curr = curr.next
            steps += 1
            if steps > 1000:
                return True
        
        return False