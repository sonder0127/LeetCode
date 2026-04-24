# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        carry = 0
        dummy = ListNode(0)
        curNode = dummy
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1 = l1.next
            
            if l2:
                carry+=l2.val
                l2 = l2.next
            
            tmp = ListNode(carry%10)
            curNode.next = tmp
            curNode = curNode.next
            carry = carry//10
        return dummy.next