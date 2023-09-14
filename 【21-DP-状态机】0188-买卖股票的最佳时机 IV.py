'''
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格，和一个整型 k 。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1：
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2：
输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

提示：
0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
'''


'''
这是一个动态规划问题

状态定义：dp[i, j, 0] 表示到第 i 天结束时，之多完成 j 笔交易，若未持有股票的最大利润
         dp[i, j, 1] 表示到第 i 天结束时，之多完成 j 笔交易，若持有股票的最大利润

分为4种情况：
1. 若第 i - 1 天结束时有股票，第 i 天结束时有股票，此时 dp[i, j, 1] = dp[i - 1, j, 1]
2. 若第 i - 1 天结束时没有股票，第 i 天结束时有股票，此时 dp[i, j, 1] = dp[i - 1, j, 0] - prices[i]
综合上述两种情况，此时 dp[i, j, 1] = max(dp[i - 1, j, 1], dp[i - 1, j, 0] - prices[i])
3. 若第 i - 1 天结束时没有股票，第 i 天结束时没有股票，此时 dp[i, j, 0] = dp[i - 1, j, 0]
4. 若第 i - 1 天结束时有股票，第 i 天结束时没有股票，此时 dp[i, j, 0] = dp[i - 1, j - 1, 1] + prices[i]
综合上述两种情况，此时 dp[i, j, 0] = max(dp[i - 1, j, 0], dp[i - 1, j - 1, 1] + prices[i])

状态转移方程：如上述分类讨论

边界条件：
dp[_, -1, _] = -inf
dp[-1, j, 0] = 0
dp[-1, j, 1] = -inf
'''


### 方法一：记忆化搜索
# 时间复杂度：O(nk)
# 空间复杂度：O(nk)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, j, hold):
            if j < 0:
                return -inf
            if i < 0:
                return 0 if hold == 0 else -inf
            if hold == 1:  # 若持有股票
                return max(dfs(i - 1, j, 1), dfs(i - 1, j, 0) - prices[i])
            return max(dfs(i - 1, j, 0), dfs(i - 1, j - 1, 1) + prices[i])  # 若未持有股票
        return dfs(n - 1, k, 0)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(nk)
# 空间复杂度：O(nk)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-inf, -inf] for _ in range(k + 2)] for _ in range(n + 1)]
        for j in range(1, k + 2):
            dp[0][j][0] = 0
        for i, x in enumerate(prices):
            for j in range(1, k + 2):
                dp[i + 1][j][1] = max(dp[i][j][1], dp[i][j][0] - x)
                dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j - 1][1] + x)
        return dp[n][k + 1][0]
    

### 方法三：空间优化，两个数组
# 时间复杂度：O(nk)
# 空间复杂度：O(k)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-inf, -inf] for _ in range(k + 2)] for _ in range(2)]
        for j in range(1, k + 2):
            dp[0][j][0] = 0
        for i, x in enumerate(prices):
            for j in range(1, k + 2):
                dp[(i + 1) % 2][j][1] = max(dp[i % 2][j][1], dp[i % 2][j][0] - x)
                dp[(i + 1) % 2][j][0] = max(dp[i % 2][j][0], dp[i % 2][j - 1][1] + x)
        return dp[n % 2][k + 1][0]