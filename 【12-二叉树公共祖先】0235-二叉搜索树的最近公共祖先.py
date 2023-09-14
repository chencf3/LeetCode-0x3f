'''
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。

示例 2:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
'''


### 方法一：递归，看作普通树，与0236相同
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in [None, p, q]:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # 左右同时存在 p 或 q 的祖先
            return root
        elif left:  # 只有左边存在 p 或 q 的祖先
            return left
        elif right:  # 只有右边存在 p 或 q 的祖先
            return right


### 方法二：递归，二叉搜索树
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in [None, p, q]:
            return root
        elif p.val < root.val < q.val or p.val > root.val > q.val:  # p 和 q 中有一个大于当前节点值，另一个小于当前节点值，则最近公共祖先为当前节点
            return root
        elif p.val < root.val and q.val < root.val:   # 当前节点值小于 p 和 q 的值，则最近公共祖先必在左子树中
            return self.lowestCommonAncestor(root.left, p, q)
        else:    # 当前节点值大于 p 和 q 的值，则最近公共祖先必在右子树中
            return self.lowestCommonAncestor(root.right, p, q)