# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 创建一个虚拟头节点（哨兵节点），val=0，next 指向原链表头
        dummy = ListNode(0)
        dummy.next = head
        
        # 2. prev 指针：永远指向【当前要交换的两个节点的前一个节点】
        prev = dummy
        
        # 3. 循环条件：必须有两个节点才能交换
        #    如果 head 为空 或 只有一个节点，就不用交换了
        while head and head.next:
            
            left = head       # 第一个要交换的节点
            right = head.next # 第二个要交换的节点
            
            # ==================== 核心：三步交换 ====================
            # 前一个节点 指向 第二个节点（right变成新头）
            prev.next = right
            
            # 第一个节点 指向 第二个节点的下一个（防止断链）
            left.next = right.next
            
            # 第二个节点 指向 第一个节点（完成交换）
            right.next = left
            # ======================================================
            
            # 4. 指针向后移动，准备下一组交换
            prev = left   # prev 来到【交换后的后一个节点】，作为下一组的前驱
            head = left.next # head 来到下一组的第一个节点
        
        # 5. dummy.next 永远是新链表的头
        return dummy.next