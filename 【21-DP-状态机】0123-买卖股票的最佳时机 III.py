'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

示例 2：
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3：
输入：prices = [7,6,4,3,1] 
输出：0 
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。

示例 4：
输入：prices = [1]
输出：0

提示：
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^5
'''


'''
这是一个动态规划问题

这题是0188-买卖股票的最佳时机 IV，k = 2的特殊情况

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
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
        return dfs(n - 1, 2, 0)


### 方法二：一比一翻译为递推
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-inf, -inf] for _ in range(4)] for _ in range(n + 1)]
        for j in range(1, 4):
            dp[0][j][0] = 0
        for i, x in enumerate(prices):
            for j in range(1, 4):
                dp[i + 1][j][1] = max(dp[i][j][1], dp[i][j][0] - x)
                dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j - 1][1] + x)
        return dp[n][3][0]
    

### 方法三：空间优化，两个数组
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-inf, -inf] for _ in range(4)] for _ in range(2)]
        for j in range(1, 4):
            dp[0][j][0] = 0
        for i, x in enumerate(prices):
            for j in range(1, 4):
                dp[(i + 1) % 2][j][1] = max(dp[i % 2][j][1], dp[i % 2][j][0] - x)
                dp[(i + 1) % 2][j][0] = max(dp[i % 2][j][0], dp[i % 2][j - 1][1] + x)
        return dp[n % 2][3][0]