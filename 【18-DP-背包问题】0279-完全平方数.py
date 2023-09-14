'''
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9
 
提示：
1 <= n <= 10^4
'''

'''
完全背包问题

本题与 0322-零钱兑换 几乎完全一致，区别仅在于 nums 需自己生成
因此直接选用最优的空间优化方法
'''


### 方法一：空间优化，一个数组
# 时间复杂度：O(n * sqrt(n))
# 空间复杂度：O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        dp = [0] + [inf] * n
        for x in nums:
            for c in range(x, n + 1):
                dp[c] = min(dp[c], dp[c - x] + 1)
        res = dp[n]
        return res if res < inf else -1