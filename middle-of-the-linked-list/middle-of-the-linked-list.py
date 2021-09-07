# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count =1
        i = j = head
        while i.next != None:
            i = i.next
            count +=1
            if count %2 ==0 :
                j  = j.next
        return j