'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]

提示：
1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
'''


### 方法一：枚举选项
# 时间复杂度：O(n * n!)
# 空间复杂度：O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, path = [], []

        def dfs(i, unvisited):
            if i == n:
                res.append(path.copy())
                return
            for c in unvisited:
                path.append(c)
                dfs(i + 1, unvisited - {c})
                path.pop()
        
        dfs(0, set(nums))
        return res