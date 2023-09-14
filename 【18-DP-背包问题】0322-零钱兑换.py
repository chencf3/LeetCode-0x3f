'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

提示：
1 <= coins.length <= 12
1 <= coins[i] <= 2 ^ 31 - 1
0 <= amount <= 10 ^ 4
'''


'''
完全背包问题

这是一个动态规划问题

状态定义：dp[i, c] 表示在前 i 种硬币中和为 c 的最少硬币个数

分为两种情况：
1. 若不选第 i 种硬币，就等于 dp[i - 1, c]
2. 若选第 i 种硬币，就等于 dp[i, c - coins[i]] + 1
在前 i 种硬币中和为 c 的最少硬币个数为上述两种情况的最少硬币个数的最小值

状态转移方程：dp[i, c] = min(dp[i - 1, c], dp[i, c - coins[i]] + 1)
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n * amount)
# 空间复杂度：O(n * amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @cache
        def dfs(i, c):
            if i < 0:  # 终止条件
                return 0 if c == 0 else inf
            if coins[i] > c:  # 超出时只能不选
                return dfs(i - 1, c)
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)  # 否则可以选，也可以不选
        
        res = dfs(n - 1, amount)
        return res if res != inf else -1


### 方法二：一比一翻译为递推
# 时间复杂度：O(n * amount)
# 空间复杂度：O(n * amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[inf] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):
            for c in range(amount + 1):
                if coins[i] > c:
                    dp[i + 1][c] = dp[i][c]
                else:
                    dp[i + 1][c] = min(dp[i][c], dp[i + 1][c - coins[i]] + 1)
        res = dp[n][amount]
        return res if res != inf else -1


### 方法三：空间优化，两个数组
# 时间复杂度：O(n * amount)
# 空间复杂度：O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[inf] * (amount + 1) for _ in range(2)]
        dp[0][0] = 0
        for i in range(n):
            for c in range(amount + 1):
                if coins[i] > c:
                    dp[(i + 1) % 2][c] = dp[i % 2][c]
                else:
                    dp[(i + 1) % 2][c] = min(dp[i % 2][c], dp[(i + 1) % 2][c - coins[i]] + 1)
        res = dp[n % 2][amount]
        return res if res != inf else -1


### 方法四：空间优化，一个数组
# 时间复杂度：O(n * amount)
# 空间复杂度：O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf] * amount
        for x in coins:
            for c in range(x, amount + 1):
                dp[c] = min(dp[c], dp[c - x] + 1)
        res = dp[amount]
        return res if res < inf else -1