# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head 
        prev = None
        nxt = curr.next
        count = -1
        len_ll = 0
        

        while curr:
            len_ll += 1
            temp = curr
            curr = nxt
            if temp.next:
                nxt = curr.next

        if len_ll == 1:
            head.val = ''
            return head
        
        curr = head
        nxt = curr.next
        prev = None
        m = len_ll - n
        while curr:
            count += 1
            if count == m:
                if prev:
                    prev.next = nxt
                    return head
                else:
                    return curr.next

            else:
                temp = curr
                curr = nxt
                if temp.next:
                    nxt = curr.next
                # else:
                #     if prev:
                #         prev.next = None
                #         return head.next
                #     else:
                #         head.val = ''
                #         return head
                prev = temp
        return head
