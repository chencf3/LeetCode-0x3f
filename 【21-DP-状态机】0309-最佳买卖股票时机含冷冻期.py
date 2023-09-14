'''
给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: prices = [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

示例 2:
输入: prices = [1]
输出: 0

提示：
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''


'''
这是一个动态规划问题

与0122-买卖股票的最佳时机 II相比，区别在于若第 i 天买入，只能考虑第 i - 2 天卖出

状态定义：dp[i, 0] 表示到第 i 天结束时，若未持有股票的最大利润
         dp[i, 1] 表示到第 i 天结束时，若持有股票的最大利润

分为4种情况：
1. 若第 i - 1 天结束时有股票，第 i 天结束时有股票，此时 dp[i, 1] = dp[i - 1, 1]
2. 若第 i - 1 天结束时没有股票，第 i 天结束时有股票，此时 dp[i, 1] = dp[i - 2, 0] - prices[i]
综合上述两种情况，此时 dp[i, 1] = max(dp[i - 1, 1], dp[i - 2, 0] - prices[i])
3. 若第 i - 1 天结束时没有股票，第 i 天结束时没有股票，此时 dp[i, 0] = dp[i - 1, 0]
4. 若第 i - 1 天结束时有股票，第 i 天结束时没有股票，此时 dp[i, 0] = dp[i - 1, 1] + prices[i]
综合上述两种情况，此时 dp[i, 0] = max(dp[i - 1, 0], dp[i - 1, 1] - prices[i])

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
        def dfs(i, hold):
            if i < 0:
                return 0 if hold == 0 else -inf
            if hold == 1:  # 若持有股票
                return max(dfs(i - 1, 1), dfs(i - 2, 0) - prices[i])
            return max(dfs(i - 1, 0), dfs(i - 1, 1) + prices[i])  # 若未持有股票
        return dfs(n - 1, 0)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, -inf] for _ in range(n + 2)]
        for i, x in enumerate(prices):
            dp[i + 2][1] = max(dp[i + 1][1], dp[i][0] - x)
            dp[i + 2][0] = max(dp[i + 1][0], dp[i + 1][1] + x)
        return dp[n + 1][0]
    

### 方法三：空间优化，三个数组
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, -inf] for _ in range(3)]
        for i, x in enumerate(prices):
            dp[(i + 2) % 3][1] = max(dp[(i + 1) % 3][1], dp[i % 3][0] - x)
            dp[(i + 2) % 3][0] = max(dp[(i + 1) % 3][0], dp[(i + 1) % 3][1] + x)
        return dp[(n + 1) % 3][0]
    

### 方法四：空间优化，三个变量
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre, f0, f1 = 0, 0, -inf
        for p in prices:
            pre, f0, f1 = f0, max(f0, f1 + p), max(f1, pre - p)
        return f0