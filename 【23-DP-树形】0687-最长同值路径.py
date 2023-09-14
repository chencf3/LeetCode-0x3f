'''
给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。
两个节点之间的路径长度 由它们之间的边数表示。

示例 1:
输入：root = [5,4,5,1,1,5]
输出：2

示例 2:
输入：root = [1,4,5,4,4,5]
输出：2

提示:
树的节点数的范围是 [0, 10^4] 
-1000 <= Node.val <= 1000
树的深度将不超过 1000
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        @cache
        def dfs(node):
            if node is None:
                return -1
            left = dfs(node.left) + 1  # 左子树最大链长
            right = dfs(node.right) + 1  # 右子树最大链长
            if node.left is not None and node.val != node.left.val:
                left = 0
            if node.right is not None and node.val != node.right.val:
                right = 0
            nonlocal res
            res = max(res, left + right)
            return max(left, right)
        
        dfs(root)
        return res