# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            return None

        dummy = ListNode()
        tail = dummy

        merged = lists[0]

        while len(lists) > 1:
            tail = dummy
            l2 = lists.pop()
            while merged and l2:
                
                if merged.val < l2.val:
                    tail.next = merged
                    merged = merged.next
                    tail = tail.next
                else:
                    tail.next = l2
                    l2 = l2.next
                    tail = tail.next
                
            if merged:
                tail.next = merged
            
            if l2:
                tail.next = l2

            merged = dummy.next

        return dummy.next

        
        
        


            


    # Input: lists = [[1,2,4],[1,3,5],[3,6]]

    # Output: []