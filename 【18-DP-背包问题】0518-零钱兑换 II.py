'''
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
假设每一种面额的硬币有无限个。 
题目数据保证结果符合 32 位带符号整数。

示例 1：
输入：amount = 5, coins = [1, 2, 5]
输出：4
解释：有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2：
输入：amount = 3, coins = [2]
输出：0
解释：只用面额 2 的硬币不能凑成总金额 3 。

示例 3：
输入：amount = 10, coins = [10] 
输出：1

提示：
1 <= coins.length <= 300
1 <= coins[i] <= 5000
coins 中的所有值 互不相同
0 <= amount <= 5000
'''


'''
完全背包问题

这是一个动态规划问题

状态定义：dp[i, c] 表示在前 i 种硬币中和为 c 的方案数

分为两种情况：
1. 若不选第 i 种硬币，就等于 dp[i - 1, c]
2. 若选第 i 种硬币，就等于 dp[i, c - coins[i]]
在前 i 种硬币中和为 c 的最少硬币个数为上述两种情况的方案数相加

状态转移方程：dp[i, c] = dp[i - 1, c] + dp[i, c - coins[i]]
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n * amount)
# 空间复杂度：O(n * amount)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @cache
        def dfs(i, c):
            if i < 0:  # 终止条件
                return 1 if c == 0 else 0
            if coins[i] > c:  # 超出时只能不选
                return dfs(i - 1, c)
            return dfs(i - 1, c) + dfs(i, c - coins[i])  # 否则可以选，也可以不选

        return dfs(n - 1, amount)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(n * amount)
# 空间复杂度：O(n * amount)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for c in range(amount + 1):
                if coins[i] > c:
                    dp[i + 1][c] = dp[i][c]
                else:
                    dp[i + 1][c] = dp[i][c] + dp[i + 1][c - coins[i]]
        return dp[n][amount]
    

### 方法三：空间优化，两个数组
# 时间复杂度：O(n * amount)
# 空间复杂度：O(amount)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for c in range(amount + 1):
                if coins[i] > c:
                    dp[(i + 1) % 2][c] = dp[i % 2][c]
                else:
                    dp[(i + 1) % 2][c] = dp[i % 2][c] + dp[(i + 1) % 2][c - coins[i]]
        return dp[n % 2][amount]


### 方法四：空间优化，一个数组
# 时间复杂度：O(n * amount)
# 空间复杂度：O(amount)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for x in coins:
            for c in range(x, amount + 1):
                dp[c] = dp[c] + dp[c - x]
        return dp[amount]