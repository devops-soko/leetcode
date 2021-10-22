# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if cur == None:
            return None
        

        while cur.next != None :
            if cur.val != cur.next.val:
                cur = cur.next
            else :   
                cur.next = cur.next.next
        return head
    
    
    
    
    