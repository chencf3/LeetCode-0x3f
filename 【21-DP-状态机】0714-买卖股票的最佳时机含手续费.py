'''
给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1：
输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
输出：8
解释：能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8

示例 2：
输入：prices = [1,3,7,5,10,3], fee = 3
输出：6

提示：
1 <= prices.length <= 5 * 10 ^ 4
1 <= prices[i] < 5 * 10 ^ 4
0 <= fee < 5 * 10^ 4
'''


'''
这是一个动态规划问题

这题与0122-买卖股票的最佳时机 II的区别是卖出股票时需要减去手续费

状态定义：dp[i, 0] 表示到第 i 天结束时，若未持有股票的最大利润
         dp[i, 1] 表示到第 i 天结束时，若持有股票的最大利润

分为4种情况：
1. 若第 i - 1 天结束时有股票，第 i 天结束时有股票，此时 dp[i, 1] = dp[i - 1, 1]
2. 若第 i - 1 天结束时没有股票，第 i 天结束时有股票，此时 dp[i, 1] = dp[i - 1, 0] - prices[i]
综合上述两种情况，此时 dp[i, 1] = max(dp[i - 1, 1], dp[i - 1, 0] - prices[i])
3. 若第 i - 1 天结束时没有股票，第 i 天结束时没有股票，此时 dp[i, 0] = dp[i - 1, 0]
4. 若第 i - 1 天结束时有股票，第 i 天结束时没有股票，此时 dp[i, 0] = dp[i - 1, 1] + prices[i] - fee
综合上述两种情况，此时 dp[i, 0] = max(dp[i - 1, 0], dp[i - 1, 1] + prices[i] - fee)

状态转移方程：如上述分类讨论

边界条件：
dp[-1, 0] = 0
dp[-1, 1] = -inf
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @cache
        def dfs(i, hold):
            if i < 0:
                return 0 if hold == 0 else -inf
            if hold == 1:  # 若持有股票
                return max(dfs(i - 1, 1), dfs(i - 1, 0) - prices[i])
            return max(dfs(i - 1, 0), dfs(i - 1, 1) + prices[i] - fee)  # 若未持有股票
        return dfs(n - 1, 0)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -inf] for _ in range(n + 1)]
        for i, x in enumerate(prices):
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - x)
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + x - fee)
        return dp[n][0]
    

### 方法三：空间优化，两个数组
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -inf] for _ in range(2)]
        for i, x in enumerate(prices):
            dp[(i + 1) % 2][1] = max(dp[i % 2][1], dp[i % 2][0] - x)
            dp[(i + 1) % 2][0] = max(dp[i % 2][0], dp[i % 2][1] + x - fee)
        return dp[n % 2][0]
    

### 方法四：空间优化，两个变量
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        f0, f1 = 0, -inf
        for p in prices:
            f0, f1 = max(f0, f1 + p - fee), max(f1, f0 - p)
        return f0


### 方法五：贪心
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = prices[0] + fee  # 买入成本
        res = 0  # 利润
        for i in range(1, n):
            if prices[i] + fee < buy:  # 买入成本可以更小，就更新买入成本
                buy = prices[i] + fee
            elif prices[i] > buy:  # 当前价格大于买入成本，就卖出
                res += prices[i] - buy
                buy = prices[i]  # 更新买入成本为当前价格
        return res