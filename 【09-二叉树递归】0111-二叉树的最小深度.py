'''
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

示例 1：
输入：root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
 
提示：
树中节点数的范围在 [0, 10^5] 内
-1000 <= Node.val <= 1000
'''


### 方法一：递归，把深度从下往上归
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth * right_depth == 0:  # 若左右子树有一个为空
            return left_depth + right_depth + 1
        return min(left_depth, right_depth) + 1  # 若左右子树均不为空
    

### 方法二：递归，更新全局变量深度值
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(node, depth):
            if node.left is None and node.right is None:
                nonlocal res
                res = min(res, depth)
                return
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        res = inf
        dfs(root, 1)
        return res
    

### 方法三：迭代，层序遍历
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = 0
        q = deque([root])
        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if node.left is None and node.right is None:
                    return res