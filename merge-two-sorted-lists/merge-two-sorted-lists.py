# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = head =  ListNode()
        while (l1 and l2) :
            if l1.val < l2.val :
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
            else :
                l3.next = l2
                l2 = l2.next
                l3 = l3.next
                
        while (l1 and l2 == None):
            l3.next = l1
            l1 = l1.next
            l3 = l3.next
            
        while (l2 and l1 == None) :
            l3.next = l2
            l2 = l2.next
            l3 = l3.next
        return head.next
        