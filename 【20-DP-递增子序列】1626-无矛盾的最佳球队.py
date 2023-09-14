'''
假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。
然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。
给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回 所有可能的无矛盾球队中得分最高那支的分数 。

示例 1：
输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
输出：34
解释：你可以选中所有球员。

示例 2：
输入：scores = [4,5,6,5], ages = [2,1,2,1]
输出：16
解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。

示例 3：
输入：scores = [1,2,3,5], ages = [8,9,10,1]
输出：6
解释：最佳的选择是前 3 名球员。

'''


'''
这是一个动态规划问题

按照分数从小到大排序，分数相同的按照年龄从小到大排序，问题等价于从 ages 中选择分数之和最大的递增子序列

状态定义：
dp[i] 表示选第 i 个玩家时，可以选择到的最大分数

状态转移方程：
dp[i] = max(dp[j]) + players[i][0]，其中 j < i 且 players[j][1] <= players[i][1]
players[i][0]：分数
players[i][1]：年龄
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n)
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = sorted(zip(scores, ages))  # 按照分数从小到大排序，分数相同的按照年龄从小到大排序
        @cache
        def dfs(i):
            res = 0
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    res = max(res, dfs(j))
            return res + players[i][0]

        return max(dfs(i) for i in range(n))


### 方法二：一比一翻译为递推
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n)
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = sorted(zip(scores, ages))  # 按照分数从小到大排序，分数相同的按照年龄从小到大排序
        dp = [0] * n
        for i in range(n):
            res = 0
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    res = max(res, dp[j])
            dp[i] = res + players[i][0]

        return max(dp)