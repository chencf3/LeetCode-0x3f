'''
给你一个整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

示例 2：
输入：nums = [1], target = 1
输出：1

提示：
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''


'''
0-1背包问题

这是一个动态规划问题

记正数和为 p，则负数和为 sum(nums) - p
表达式的值为 p - (sum(nums) - p) == 2 * p - sum(nums) == target
=> p = (target + sum(nums)) / 2
因此 target + sum(nums) 为正数，且为偶数
转化为寻找若干个数求和等于 p

状态定义：dp[i, c] 表示在前 i 个数字中和为 c 的方案数

分为两种情况：
1. 若不选第 i 个数，就等于 dp[i - 1, c]
2. 若选第 i 个数，就等于 dp[i - 1, c - nums[i]]
在前 i 个数字中和为 c 的方案数为上述两种情况的方案数相加

状态转移方程：dp[i, c] = dp[i - 1, c] + dp[i - 1, c - nums[i]]
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n * target)
# 空间复杂度：O(n * target)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        target += sum(nums)
        if target < 0 or target % 2 == 1:
            return 0
        target //= 2
        
        @cache
        def dfs(i, c):
            if i < 0:  # 终止条件
                return 1 if c == 0 else 0
            if nums[i] > c:  # 超出时只能不选
                return dfs(i - 1, c)
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])  # 否则可以选，也可以不选
        
        return dfs(n - 1, target)


### 方法二：一比一翻译为递推
# 时间复杂度：O(n * target)
# 空间复杂度：O(n * target)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        target += sum(nums)
        if target < 0 or target % 2 == 1:
            return 0
        target //= 2
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):  # 每一行
            for c in range(target + 1):  # 每一列
                if nums[i] > c:
                    dp[i + 1][c] = dp[i][c]
                else:
                    dp[i + 1][c] = dp[i][c] + dp[i][c - nums[i]]
        return dp[n][target]


### 方法三：空间优化，两个数组
# 时间复杂度：O(n * target)
# 空间复杂度：O(target)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        target += sum(nums)
        if target < 0 or target % 2 == 1:
            return 0
        target //= 2
        dp = [[0] * (target + 1) for _ in range(2)]
        dp[0][0] = 1
        for i in range(n):  # 每一行
            for c in range(target + 1):  # 每一列
                if nums[i] > c:
                    dp[(i + 1) % 2][c] = dp[i % 2][c]
                else:
                    dp[(i + 1) % 2][c] = dp[i % 2][c] + dp[i % 2][c - nums[i]]
        return dp[n % 2][target]


### 方法四：空间优化，一个数组
# 时间复杂度：O(n * target)
# 空间复杂度：O(target)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2 == 1:
            return 0
        target //= 2
        dp = [1] + [0] * target
        for x in nums:
            for c in range(target, x - 1, -1):
                dp[c] += dp[c - x]
        return dp[target]