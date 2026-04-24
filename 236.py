def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # 递归终止条件：
    # 1. 到底了（空节点）
    # 2. 找到了 p 或 q，直接返回，不再往下搜
    if root in (None, p, q):
        return root

    # ******************************
    # 开始递归：先左、再右
    # ******************************
    left = self.lowestCommonAncestor(root.left, p, q)   # 查左子树
    right = self.lowestCommonAncestor(root.right, p, q) # 查右子树

    # 如果左边找到一个目标，右边也找到一个目标
    # → 当前节点就是它们的公共祖先！
    if left and right:
        return root

    # 否则：哪边有答案返回哪边
    # left 有 → 返回 left
    # right 有 → 返回 right
    # 都没有 → 返回 None
    return left or right