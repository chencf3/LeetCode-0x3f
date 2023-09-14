'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 400
'''


'''
这是一个动态规划问题

状态定义：dp[i] 表示到第 i 个房屋的最大金额

分为两种情况：
1. 若不偷第 i 个房屋，则可偷第 i - 1 个房屋，此时最大金额等于 dp[i - 1]
2. 若偷第 i 个房屋，则可偷第 i - 2 个房屋，此时最大金额等于 dp[i - 2] + nums[i]
第 i 个房屋的最大金额应为上述两种情况的最大值
状态转移方程：dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n)，状态个数 * 单个状态所需要的时间
# 空间复杂度：O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            if i < 0:
                return 0
            return max(dfs(i - 1), dfs(i - 2) + nums[i])
        return dfs(n - 1)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n):
            dp[i + 2] = max(dp[i + 1], dp[i] + nums[i])
        return dp[-1]


### 方法三：空间优化
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        left, right = 0, 0
        for num in nums:
            left, right = right, max(right, left + num)
        return right