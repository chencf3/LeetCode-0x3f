'''
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
返回 你能获得的 最大 利润 。

示例 1：
输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
     总利润为 4 + 3 = 7 。

示例 2：
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     总利润为 4 。

示例 3：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0 。
'''


'''
这是一个动态规划问题

状态定义：dp[i, 0] 表示到第 i 天结束时，若未持有股票的最大利润
         dp[i, 1] 表示到第 i 天结束时，若持有股票的最大利润

分为4种情况：
1. 若第 i - 1 天结束时有股票，第 i 天结束时有股票，此时 dp[i, 1] = dp[i - 1, 1]
2. 若第 i - 1 天结束时没有股票，第 i 天结束时有股票，此时 dp[i, 1] = dp[i - 1, 0] - prices[i]
综合上述两种情况，此时 dp[i, 1] = max(dp[i - 1, 1], dp[i - 1, 0] - prices[i])
3. 若第 i - 1 天结束时没有股票，第 i 天结束时没有股票，此时 dp[i, 0] = dp[i - 1, 0]
4. 若第 i - 1 天结束时有股票，第 i 天结束时没有股票，此时 dp[i, 0] = dp[i - 1, 1] + prices[i]
综合上述两种情况，此时 dp[i, 0] = max(dp[i - 1, 0], dp[i - 1, 1] + prices[i])

状态转移方程：如上述分类讨论

边界条件：
dp[-1, 0] = 0
dp[-1, 1] = -inf
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, j):
            if i < 0:
                return 0 if j == 0 else -inf
            if j == 1:  # 若持有股票
                return max(dfs(i - 1, 1), dfs(i - 1, 0) - prices[i])
            return max(dfs(i - 1, 0), dfs(i - 1, 1) + prices[i])  # 若未持有股票
        return dfs(n - 1, 0)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 1)]
        dp[0] = [0, -inf]
        for i, x in enumerate(prices):
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - x)
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + x)
        return dp[n][0]
    

### 方法三：空间优化，两个数组
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(2)]
        dp[0] = [0, -inf]
        for i, x in enumerate(prices):
            dp[(i + 1) % 2][1] = max(dp[i % 2][1], dp[i % 2][0] - x)
            dp[(i + 1) % 2][0] = max(dp[i % 2][0], dp[i % 2][1] + x)
        return dp[n % 2][0]
    

### 方法四：空间优化，两个变量
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f0, f1 = 0, -inf
        for p in prices:
            f0, f1 = max(f0, f1 + p), max(f1, f0 - p)
        return f0


### 方法五：贪心，计算每一天与前一天的差值，若差值大于0，计入结果
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res