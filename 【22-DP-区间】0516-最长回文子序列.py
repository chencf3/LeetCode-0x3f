'''
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

示例 1：
输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。

示例 2：
输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。

提示：
1 <= s.length <= 1000
s 仅由小写英文字母组成
'''


'''
这是一个动态规划问题

状态定义：dp[i, j] 表示从第 i 个数到第 j 个数的最长回文子序列

分为2种情况：
1. 若s[i] == s[j]，此时 dp[i, j] = dp[i + 1, j - 1] + 2
2. 若s[i] != s[j]，此时 dp[i, j] = max(dp[i + 1, j], dp[i, j - 1])

状态转移方程：如上述分类讨论

边界条件：
dp[i, i] = 1
dp[i + 1, i] = 0
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n ^ 2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2
            return max(dfs(i, j - 1), dfs(i + 1, j))
        return dfs(0, n - 1)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n ^ 2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][n - 1]
    

### 方法三：空间优化
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            pre = 0
            for j in range(i + 1, n):
                tmp = dp[j]
                dp[j] = pre + 2 if s[i] == s[j] else max(dp[j], dp[j - 1])
                pre = tmp
        return dp[-1]