'''
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

提示：
1 <= nums.length <= 200
1 <= nums[i] <= 100
'''


'''
0-1背包问题

这是一个动态规划问题

状态定义：dp[i, c] 表示在前 i 个数字中是否存在和为 c 的方案

分为两种情况：
1. 若不选第 i 个数，就等于 dp[i - 1, c]
2. 若选第 i 个数，就等于 dp[i - 1, c - nums[i]]
在前 i 个数字中和为 c 的方案数为上述两种情况的方案数取或运算

状态转移方程：dp[i, c] = dp[i - 1, c] or dp[i - 1, c - nums[i]]
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n * nums)
# 空间复杂度：O(n * nums)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target < 0 or target % 2 != 0:
            return False
        target //= 2
        n = len(nums)

        @cache
        def dfs(i, c):
            if i < 0:  # 终止条件
                return c == 0
            if nums[i] > c:  # 超出时只能不选
                return dfs(i - 1, c)
            return dfs(i - 1, c) or dfs(i - 1, c - nums[i])  # 否则可以选，也可以不选
        
        return dfs(n - 1, target)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(n * nums)
# 空间复杂度：O(n * nums)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target < 0 or target % 2 != 0:
            return False
        target //= 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(n):  # 每一行
            for c in range(target + 1):  # 每一列
                if nums[i] > c:
                    dp[i + 1][c] = dp[i][c]
                else:
                    dp[i + 1][c] = dp[i][c] or dp[i][c - nums[i]]
        return dp[n][target]
    

### 方法三：空间优化，两个数组
# 时间复杂度：O(n * nums)
# 空间复杂度：O(nums)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target < 0 or target % 2 != 0:
            return False
        target //= 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(2)]
        dp[0][0] = True
        for i in range(n):  # 每一行
            for c in range(target + 1):  # 每一列
                if nums[i] > c:
                    dp[(i + 1) % 2][c] = dp[i % 2][c]
                else:
                    dp[(i + 1) % 2][c] = dp[i % 2][c] or dp[i % 2][c - nums[i]]
        return dp[n % 2][target]


### 方法四：空间优化，一个数组
# 时间复杂度：O(n * nums)
# 空间复杂度：O(nums)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target < 0 or target % 2 != 0:
            return False
        target //= 2
        n = len(nums)
        dp = [True] + [False] * target
        for x in nums:
            for c in range(target, x - 1, -1):
                dp[c] = dp[c] or dp[c - x]
        return dp[target]