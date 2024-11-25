# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next is None:
            return False
        fast = head
        slow = head
        while fast and fast.next is not None:
            if fast.next == slow:
                return True 
            else:
                fast = fast.next.next
                slow = slow.next
        return False

        