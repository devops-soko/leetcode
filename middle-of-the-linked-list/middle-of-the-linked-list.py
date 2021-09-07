# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = j = head
        count = 1
        while i.next != None :
            i = i.next
            count +=1
            
            if count %2 ==0:
                j = j.next
        return j