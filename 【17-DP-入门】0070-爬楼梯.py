'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

提示：
1 <= n <= 45
'''


'''
这是一个动态规划问题

状态定义：dp[i] 表示走到第 i 个台阶的方案数
分为两种情况：
1. 若选第 i - 1 个台阶，此时方案数等于 dp[i - 1]
2. 若不选第 i - 1 个台阶，则必选第 i - 2 个台阶，此时方案数等于 dp[i - 2]
走到第 i 个台阶的方案数应为上述两种情况的方案数求和

状态转移方程：dp[i] = dp[i - 1] + dp[i - 2]
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i):
            if i <= 2:
                return i
            return dfs(i - 1) + dfs(i - 2)

        return dfs(n)


### 方法二：一比一翻译为递推
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1, 2] + [0] * (n - 2)
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
    

### 方法三：空间优化
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        left, right = 1, 2
        for _ in range(n - 2):
            left, right = right, left + right
        return right