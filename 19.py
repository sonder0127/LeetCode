# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. 求链表长度（你写的）
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        # 2. 计算要走的步数（你写的）
        step = length - n
        cur = head
        
        # 特殊情况：如果删的是头节点！
        if step == 0:
            return head.next
        
        # 3. 走到被删节点的前一个（你写的）
        while step > 1:
            cur = cur.next
            step -= 1
        
        # 4. 【你缺的核心：删除节点】
        cur.next = cur.next.next
        
        return head
