# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def into_str(head: ListNode) -> str :
            while head:
                if head == None:
                    return ''

                if head.next == None :
                    return str(head.val)
                return str(head.val) + into_str(head.next)

        return int(into_str(head),2)
    
    
    
    