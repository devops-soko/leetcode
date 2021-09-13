# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        check = set()
        cur = head
        while cur != None :
            if cur in check:
                return True
            check.add(cur)
            cur = cur.next
        return False