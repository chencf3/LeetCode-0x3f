'''
给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
如果树中有不止一个众数，可以按 任意顺序 返回。
假定 BST 满足如下定义：
结点左子树中所含节点的值 小于等于 当前节点的值
结点右子树中所含节点的值 大于等于 当前节点的值
左子树和右子树都是二叉搜索树

示例 1：
输入：root = [1,null,2,2]
输出：[2]

示例 2：
输入：root = [0]
输出：[0]

提示：
树中节点的数目在范围 [1, 10^4] 内
-10^5 <= Node.val <= 10^5

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
'''


### 方法一：中序遍历，计数
# 时间复杂度：O(n)
# 空间复杂度：O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        dic = Counter()
        def inOrder(node):
            if node:
                inOrder(node.left)
                dic[node.val] += 1
                inOrder(node.right)
                
        inOrder(root)
        d = defaultdict(list)
        for k, v in dic.items():
            d[v].append(k)
        return d[max(d.keys())]