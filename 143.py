# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def middleNode(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverseList(head):
            prev = None
            cur = head
            while cur:
                nextNode = cur.next
                cur.next = prev
                prev = cur
                cur = nextNode
            return prev
        
        mid_head = middleNode(head)
        head2 = reverseList(mid_head)
        head1 = head
        while head2.next:
            next1 = head1.next
            next2 = head2.next
            head1.next = head2
            head2.next = next1
            head1 = next1
            head2 = next2

