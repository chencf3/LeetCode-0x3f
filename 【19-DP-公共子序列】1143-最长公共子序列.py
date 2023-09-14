'''
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

示例 1：
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。

示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。

提示：
1 <= text1.length, text2.length <= 1000
text1 和 text2 仅由小写英文字符组成。
'''


'''
这是一个动态规划问题

状态定义：dp[i, j] 表示 text1[:i + 1] 和 text2[:j + 1] 的最长公共子序列长度。

分为两种情况：
1. 若 text1[i] == text2[j]，等于 dp[i - 1, j - 1] + 1
2. 若 text1[i] != text2[j]，等于 max(dp[i, j - 1]], dp[i - 1, j])

状态转移方程：如上述分类讨论
'''


### 方法一：记忆化搜索
# 时间复杂度：O(nm)
# 空间复杂度：O(nm)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))

        return dfs(n - 1, m - 1)


### 方法二：一比一翻译为递推
# 时间复杂度：O(nm)
# 空间复杂度：O(nm)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[n][m]


### 方法三：空间优化，两个数组
# 时间复杂度：O(nm)
# 空间复杂度：O(m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(2)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[(i + 1) % 2][j + 1] = dp[i % 2][j] + 1
                else:
                    dp[(i + 1) % 2][j + 1] = max(dp[i % 2][j + 1], dp[(i + 1) % 2][j])
        return dp[n % 2][m]
    

### 方法四：空间优化，一个数组
# 时间复杂度：O(nm)
# 空间复杂度：O(m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for x in text1:
            pre = 0
            for j, y in enumerate(text2):
                tmp = dp[j + 1]
                dp[j + 1] = pre + 1 if x == y else max(dp[j + 1], dp[j])
                pre = tmp
        return dp[-1]