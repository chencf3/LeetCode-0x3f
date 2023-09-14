'''
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
差值是一个正数，其数值等于两值之差的绝对值。

示例 1：
输入：root = [4,2,6,1,3]
输出：1

示例 2：
输入：root = [1,0,48,null,null,12,49]
输出：1

提示：
树中节点的数目范围是 [2, 10^4]
0 <= Node.val <= 10^5
'''


### 方法一：中序遍历，与前面的值相比较
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        def inOrder(node):
            if node:
                inOrder(node.left)
                values.append(node.val)
                inOrder(node.right)

        inOrder(root)
        return min([values[i] - values[i - 1] for i in range(1, len(values))])