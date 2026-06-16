# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # here we use floyd's tortoise & hare where
        # there exists a slow pointer and fast pointer
        # if list is circular, pointers will meet at some point
        # closing gap can only be equal to len(linkedlist)

        hashSet = {}
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

        