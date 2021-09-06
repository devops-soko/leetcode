# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        def str_linked_list(head: ListNode) -> str :
            if head == None :
                return ''
            elif head.next == None :
                return str(head.val)
            return str(head.val) + str_linked_list(head.next)
        
        return int(str_linked_list(head), 2)