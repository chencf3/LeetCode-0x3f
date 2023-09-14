'''
一个下标从 0 开始的数组的 交替和 定义为 偶数 下标处元素之 和 减去 奇数 下标处元素之 和 。
比方说，数组 [4,2,5,3] 的交替和为 (4 + 5) - (2 + 3) = 4 。
给你一个数组 nums ，请你返回 nums 中任意子序列的 最大交替和 （子序列的下标 重新 从 0 开始编号）。
一个数组的 子序列 是从原数组中删除一些元素后（也可能一个也不删除）剩余元素不改变顺序组成的数组。比方说，[2,7,4] 是 [4,2,3,7,2,1,4] 的一个子序列（加粗元素），但是 [2,4,2] 不是。

示例 1：
输入：nums = [4,2,5,3]
输出：7
解释：最优子序列为 [4,2,5] ，交替和为 (4 + 5) - 2 = 7 。

示例 2：
输入：nums = [5,6,7,8]
输出：8
解释：最优子序列为 [8] ，交替和为 8 。

示例 3：
输入：nums = [6,2,1,2,4,5]
输出：10
解释：最优子序列为 [6,1,5] ，交替和为 (6 + 5) - 1 = 10 。

提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''


'''
这是一个动态规划问题

状态定义：dp[i, 0] 表示到第 i 个数时，子序列长度为偶数的最大交替和
         dp[i, 1] 表示到第 i 个数时，子序列长度为奇数的最大交替和

分为4种情况：
1. 若第 i - 1 个数时子序列长度为偶数，第 i 个数时子序列长度为偶数，此时 dp[i, 0] = dp[i - 1, 0]
2. 若第 i - 1 个数时子序列长度为奇数，第 i 个数时子序列长度为偶数，此时 dp[i, 0] = dp[i - 1, 1] - nums[i]
综合上述两种情况，此时 dp[i, 0] = max(dp[i - 1, 0], dp[i - 1, 1] - nums[i])
3. 若第 i - 1 个数时子序列长度为奇数，第 i 个数时子序列长度为奇数，此时 dp[i, 1] = dp[i - 1, 1]
4. 若第 i - 1 个数时子序列长度为偶数，第 i 个数时子序列长度为奇数，此时 dp[i, 1] = dp[i - 1, 0] + nums[i]
综合上述两种情况，此时 dp[i, 1] = max(dp[i - 1, 1], dp[i - 1, 0] + nums[i])

状态转移方程：如上述分类讨论

边界条件：
dp[-1, 0] = 0
dp[-1, 1] = -inf
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i, j):
            if i < 0:
                return 0 if j == 0 else -inf
            if j == 1:  # 第 i 个数时子序列长度为奇数
                return max(dfs(i - 1, 1), dfs(i - 1, 0) + nums[i])
            return max(dfs(i - 1, 0), dfs(i - 1, 1) - nums[i])  # 第 i 个数时子序列长度为偶数
        return dfs(n - 1, 1)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, -inf] for _ in range(n + 1)]
        for i, x in enumerate(nums):
            dp[i + 1][1] = max(dp[i][1], dp[i][0] + x)
            dp[i + 1][0] = max(dp[i][0], dp[i][1] - x)
        return dp[n][1]
    

### 方法三：空间优化，两个数组
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, -inf] for _ in range(2)]
        for i, x in enumerate(nums):
            dp[(i + 1) % 2][1] = max(dp[i % 2][1], dp[i % 2][0] + x)
            dp[(i + 1) % 2][0] = max(dp[i % 2][0], dp[i % 2][1] - x)
        return dp[n % 2][1]
    

### 方法四：空间优化，两个变量
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        f0, f1 = 0, -inf
        for num in nums:
            f0, f1 = max(f0, f1 - num), max(f1, f0 + num)
        return f1