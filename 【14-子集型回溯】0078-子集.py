'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

提示：
1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
'''


### 方法一：选或不选
# 时间复杂度：O(n * 2 ^ n)
# 空间复杂度：O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        n = len(nums)
        def dfs(i):
            if i == n:  # 终止条件
                res.append(path.copy())  # path是全局变量，需要用copy保存下来
                return
            # 可以不选当前数字
            dfs(i + 1)
            # 也可以选当前数字
            path.append(nums[i])
            dfs(i + 1)
            path.pop()  # path是全局变量，需要恢复现场
        dfs(0)
        return res
    

### 方法二：枚举选项
# 时间复杂度：O(n * 2 ^ n)
# 空间复杂度：O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        n = len(nums)
        def dfs(i):
            res.append(path.copy())  # 每次都要保存答案，path是全局变量，需要用copy保存下来
            if i == n:  # 终止条件
                return
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()  # path是全局变量，需要恢复现场
        dfs(0)
        return res