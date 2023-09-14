'''
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
叶子节点 是指没有子节点的节点。

示例 1：
输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]

示例 2：
输入：root = [1]
输出：["1"]

提示：
树中节点的数目在范围 [1, 100] 内
-100 <= Node.val <= 100
'''


### 方法一：递归
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n ^ 2)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if node is None:
                return
            if node.left is None and node.right is None:
                nonlocal res
                res.append(path + str(node.val))
                return
            dfs(node.left, path + str(node.val) + '->')
            dfs(node.right, path + str(node.val) + '->')

        res = []
        dfs(root, '')
        return res