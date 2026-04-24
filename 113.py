# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        #O(n^2),O(n)
        path_list = []
        path = []

        def dfs(node, left):
            if not node:
                return
            path.append(node.val)
            left -= node.val
            #当前的是叶子节点，才会触发
            if not node.left and not node.right and left==0:
                path_list.append(path.copy())
            else:
                dfs(node.left, left)
                dfs(node.right, left)
            path.pop()
        dfs(root, targetSum)
        return path_list