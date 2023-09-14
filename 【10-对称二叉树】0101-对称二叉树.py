'''
给你一个二叉树的根节点 root ， 检查它是否轴对称。

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false

提示：
树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100

进阶：你可以运用递归和迭代两种方法解决这个问题吗？
'''


### 方法一：递归
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p is None or q is None:
                return p == q
            return p.val == q.val and isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

        return isSameTree(root.left, root.right)
    

### 方法二：迭代，BFS
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = deque()
        q.append((root, root))
        while q:
            l, r = q.popleft()
            if l is None and r is None:
                continue
            if l is None or r is None or l.val != r.val:
                return False
            q.append((l.left, r.right))
            q.append((l.right, r.left))
        return True