'''
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1：
输入：root = [2,1,3]
输出：true

示例 2：
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。

提示：
树中节点数目范围在[1, 104] 内
-2^31 <= Node.val <= 2^31 - 1
'''


### 方法一：前序遍历：先取节点值，往下传更新范围
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, x, y):
            # 函数定义：node 的值是否在 (x, y) 范围内，且左右子树是否为二叉搜索树
            if node is None:
                return True
            return x < node.val < y and dfs(node.left, x, node.val) and dfs(node.right, node.val, y)

        return dfs(root, -inf, inf)
        
        
### 方法二：中序遍历：中序遍历二叉搜索树有序
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        def inOrder(node):
            if node:
                inOrder(node.left)
                values.append(node.val)
                inOrder(node.right)

        inOrder(root)
        return all(values[i - 1] < values[i] for i in range(1, len(values)))

        
### 方法三：后序遍历，把左右子树的取值范围和节点取值往上传（没有完全理解）
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return inf, -inf
            x = node.val
            l_min, l_max = dfs(node.left)
            if x <= l_max:
                return -inf, inf
            r_min, r_max = dfs(node.right)
            if x >= r_min:
                return -inf, inf
            return min(l_min, x), max(r_max, x)
        return dfs(root)[1] != inf