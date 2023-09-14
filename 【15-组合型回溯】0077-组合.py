'''
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。

示例 1：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

示例 2：
输入：n = 1, k = 1
输出：[[1]]

提示：
1 <= n <= 20
1 <= k <= n
'''


'''
回溯问题的时间复杂度 = 路径长度 × 搜索树的叶子数
'''


### 方法一：选或不选
# 时间复杂度：O(k * C(n, k))
# 空间复杂度：O(k)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, path = [], []
        def dfs(i):
            d = k - len(path)  # 还要选d个数
            if d == 0:  # 终止条件
                res.append(path.copy())  # 保存答案
                return
            if i < d:  # 如果可以选的数小于d，剪枝
                return
            # 不选当前的数字
            dfs(i - 1)
            # 选当前的数字
            path.append(i)
            dfs(i - 1)
            path.pop()  # 恢复现场
        dfs(n)  # 倒序取数
        return res
    

### 方法二：枚举答案
# 时间复杂度：O(k * C(n, k))
# 空间复杂度：O(k)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, path = [], []
        def dfs(i):
            d = k - len(path)  # 还要选d个数
            if d == 0:  # 终止条件
                res.append(path.copy())  # 保存答案
                return
            if i < d:  # 如果可以选的数小于d，剪枝
                return
            for j in range(i, 0, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()  # 恢复现场
        dfs(n)  # 倒序取数
        return res