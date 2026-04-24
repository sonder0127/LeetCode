"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 哈希表（字典）：key 是原节点，value 是复制出来的新节点
        # 作用：记录已经复制过的节点，避免重复创建
        cachedNode = {}
        
        def dfs(node):
            if not node:
                return None
            # 如果当前节点**还没有被复制过**
            if node not in cachedNode:
                new_node = Node(node.val)
                # 2. 把「原节点:新节点」存到哈希表里，标记已复制
                cachedNode[node] = new_node
                new_node.next = dfs(node.next)
                new_node.random = dfs(node.random)
            
            # 如果节点已经复制过，直接从哈希表中返回对应的新节点
            return cachedNode[node]
        
        # 从链表头节点开始递归
        return dfs(head)